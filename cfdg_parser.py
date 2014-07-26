#  Jordan Cazamias
#  CFDG Optimizer
#  April 2014

import copy
import re
import sys
import string

from grammar import *

WILDCARD = r"\*"

# Patterns for parsing CFDG files
startshape_pattern = r"\s*startshape\s+(?P<startshapename>\w+)\n"
shape_header_pattern = r"\s*(?<!start)shape\s+(?P<shapename>\w+)"
rule_header_pattern = r"\s*rule\s*"
rule_weight_pattern = r"(?P<rulefixed>{0}?)\s*(?P<ruleweight>[\d\.]*)\s*".format(WILDCARD)
rule_body_pattern = r"(?:\n\s*\{|\{)\n?(?P<rulebody>(?:[^\}]*\n?)+)\s*\}"

startshape_regex = re.compile(startshape_pattern)
shape_header_regex = re.compile(shape_header_pattern)
rule_weight_regex = re.compile(rule_weight_pattern)
single_rule_header_regex = re.compile(shape_header_pattern +
                                      rule_weight_pattern)
single_rule_regex = re.compile(shape_header_pattern +
                               rule_weight_pattern +
                               rule_body_pattern)
rule_header_regex = re.compile(rule_header_pattern +
                               rule_weight_pattern)
rule_regex = re.compile(rule_header_pattern +
                        rule_weight_pattern +
                        rule_body_pattern)


def grammar_from_file(filename):
    # Use filename with extension stripped off
    extension = string.rfind(filename, ".cfdg")
    if extension == -1:
        grammarname = filename
    else:
        grammarname = filename[0:extension]

    return grammar_from_string(_read_file(filename), grammarname)


def grammar_from_string(grammartext, grammarname=None):
    if grammarname is None:
        grammarname = raw_input("Enter a name for grammar: '{0}...'".format(grammartext[0:20]))

    gram = Grammar(grammarname, grammartext)
    rules = []
    shapes = []
    clean_body = ""

    # Extract startshape
    startshapematch = startshape_regex.search(grammartext)
    if not startshapematch:
        raise Exception("Error: Could not find start shape")
    startshape = Shape(startshapematch.groupdict()["startshapename"])

    # Extract all shapes and rules
    shapematches = list(shape_header_regex.finditer(grammartext))
    print "Shape matches: {0}".format(len(shapematches))

    for i in range(len(shapematches)):
        shapematch = shapematches[i]
        shapename = shapematch.groupdict()["shapename"]
        print "found shape '{0}'".format(shapename)
        shape = Shape(shapematch.groupdict()["shapename"])
        shapes.append(shape)

        # Extract all rules for shape
        if i < len(shapematches) - 1:
            nextshapematch = shapematches[i+1]
            nextshapestart = nextshapematch.start()
        else:
            nextshapestart = len(grammartext)

        singlerulematch = single_rule_regex.search(grammartext, shapematch.start(), nextshapestart)
        if singlerulematch:
            # Shape has only one rule
            rulematches = [singlerulematch]
        else:
            rulematches = list(rule_regex.finditer(grammartext, shapematch.end(), nextshapestart))

        # create rule for each match
        print "\t{0} rule{1} found for shape '{2}'\n".format(
            len(rulematches), "" if len(rulematches) == 1 else "s", shapename)
        for match in rulematches:
            #weightstr = match.groupdict()["ruleweight"]
            if "ruleweight" in match.groupdict() and match.groupdict()["ruleweight"] != "":
                weight = float(match.groupdict()["ruleweight"])
            else:
                weight = 1.0

            rulebody = match.group(0)
            fixed = ("rulefixed" not in match.groupdict() or
                     match.groupdict()["rulefixed"] == "")
            #if not fixed:
            #    print "rulefixed: '{0}'".format(repr(match.groupdict()["rulefixed"]))
            newrule = Rule(rulebody, weight, fixed)
            rules.append(newrule)
            shape.rules.append(newrule)

    gram.shapes = shapes
    gram.rules = rules
    gram.startshape = startshape

    return gram

# Returns grammar body that can be parsed by CFDG
def clean_body(grammar):
    newbody = copy.deepcopy(grammar.body)
    wildcard_regex = re.compile(r"{0}\s*".format(WILDCARD))

    def remove_wildcard(match):
        wildcard_match = wildcard_regex.search(
            newbody, match.start(), match.end())

        if wildcard_match is None:
            return newbody

        string = wildcard_regex.sub(repl="", string=newbody, count=1)
        return string

    # Remove all WILDCARD markers in rule headers

    #for rulematch in reversed(list(single_rule_regex.finditer(newbody))):
    #    newbody = remove_wildcard(rulematch)
    #for rulematch in reversed(list(rule_regex.finditer(newbody))):
    #    newbody = remove_wildcard(rulematch)

    #TODO: Fix this so it doesn't remove all asterisks in grammar body
    newbody = wildcard_regex.sub(repl="", string=newbody)

    return newbody


def _read_file(filename):
    f = open(filename, 'r')

    try:
        lines = f.readlines()
    finally:
        f.close()

    filebody = "".join(lines)
    return filebody


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python {0} <path to grammar file>".format(sys.argv[0])
        print "Note: grammar must be a Context Free v3 file"
        sys.exit(0)

    grammarpath = sys.argv[1]
    g = grammar_from_file(grammarpath)

    print "fixed:"
    print [rule.fixed for rule in g.rules]

    print "weights:"
    print [rule.weight for rule in g.rules]
    print g
    #s = _read_file("grammars/clouds.cfdg")
    #m = re.search(startshape_header_regex, s)
    #print m.groupdict()
