#  Jordan Cazamias
#  CFDG Optimizer
#  April 2014

import re
import sys
import string
from grammar import *

startshape_pattern = r"\s*startshape\s+(?P<startshapename>\w+)\n"
shape_header_pattern = r"\s*(?<!start)shape\s+(?P<shapename>\w+)"
rule_header_pattern = r"\s*rule\s+"
rule_weight_pattern = r"(?P<rulefixed>\*)?\s*(?P<ruleweight>[\d\-\.]*)\s*"
rule_body_pattern = r"(?:\n\s*\{|\{)\n?(?P<rulebody>(?:[^\}]*\n?)+)\s*\}"

startshape_regex = re.compile(startshape_pattern)
shape_header_regex = re.compile(shape_header_pattern)
single_rule_regex = re.compile(shape_header_pattern + rule_weight_pattern + rule_body_pattern)
rule_regex = re.compile(rule_header_pattern + rule_weight_pattern + rule_body_pattern)


def grammar_from_file(filename):
    # Use filename with extension stripped off
    extension = string.rfind(filename, ".cfdg")
    if extension == -1:
        grammarname = filename
    else:
        grammarname = filename[0:extension]

    return grammar_from_string(read_file(filename), grammarname)


def grammar_from_string(string, grammarname=None):
    if grammarname is None:
        grammarname = raw_input("Enter a name for grammar: '{0}...'".format(string[0:20]))

    gram = Grammar(grammarname, string)
    rules = []
    shapes = []

    # Extract startshape
    startshapematch = startshape_regex.search(string)
    if not startshapematch:
        print "Error: Could not find start shape"
        raise Exception
    startshape = Shape(startshapematch.groupdict()["startshapename"])

    # Extract all shapes and rules
    shapematches = list(shape_header_regex.finditer(string))
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
            nextshapestart = len(string)

        singlerulematch = single_rule_regex.search(string, shapematch.start(), nextshapestart)
        if singlerulematch:
            # Shape has only one rule
            rulematches = [singlerulematch]
        else:
            rulematches = list(rule_regex.finditer(string, shapematch.end(), nextshapestart))

        # create rule for each match
        print "\t{0} rule{1} found for shape '{2}'\n".format(
            len(rulematches), "" if len(rulematches) == 1 else "s", shapename)
        for match in rulematches:
            weightstr = match.groupdict()["ruleweight"]
            if weightstr == "":
                weight = 1.0
            else:
                weight = float(weightstr)
            rulebody = match.group(0)
            fixed = (match.groupdict()["rulefixed"] is None)
            rule = Rule(rulebody, weight, fixed)
            rules.append(rule)
            shape.rules.append(rule)

    gram.shapes = shapes
    gram.rules = rules
    gram.startshape = startshape

    return gram


def read_file(filename):
    f = open(filename, 'r')

    try:
        lines = f.readlines()
    finally:
        f.close()

    string = "".join(lines)
    return string


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
    #s = read_file("grammars/clouds.cfdg")
    #m = re.search(startshape_header_regex, s)
    #print m.groupdict()
