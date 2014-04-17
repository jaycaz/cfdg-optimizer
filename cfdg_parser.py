#  Jordan Cazamias
#  CFDG Optimizer
#  April 2014

import re
from grammar import *

startshape_regex = r"\s*startshape\s+(?P<startshapename>\w+)\n"
shape_regex = r"\s*(?<!start)shape\s+(?P<shapename>\w+)"
single_rule_regex = shape_regex + r"\s*(?:\n\s*\{|\{)\n?(?:[^\}]*\n?)+\s*\}"
rule_regex = "\s*rule\s+(?P<ruleweight>[\d\-\.]*\s*)(?:\n\s*\{|\{)\n?(?:[^\}]*\n?)+\s*\}"


def grammar_from_file(filename):
    return grammar_from_string(read_file(filename))

def grammar_from_string(string):
    g = Grammar()
    return g

def read_file(filename):
    f = open(filename, 'r')

    try:
        lines = f.readlines()
    finally:
        f.close()

    string = "".join(lines)
    return string


if __name__ == "__main__":
    g = grammar_from_file("grammars/clouds.cfdg")
    print g
