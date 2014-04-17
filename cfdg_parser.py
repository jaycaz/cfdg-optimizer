#  Jordan Cazamias
#  CFDG Optimizer
#  April 2014

import re

startshape_regex = r"\s*startshape\s+(?P<startshapename>\w+)\n"
shape_regex = r"\s*(?<!start)shape\s+(?P<shapename>\w+)"
single_rule_regex = shape_regex + r"\s*(?:\n\s*\{|\{)\n?(?:[^\}]*\n?)+\s*\}"
rule_regex = "\s*rule\s+(?P<ruleweight>[\d\-\.]*\s*)(?:\n\s*\{|\{)\n?(?:[^\}]*\n?)+\s*\}"


