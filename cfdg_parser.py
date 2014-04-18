#  Jordan Cazamias
#  CFDG Optimizer
#  April 2014

import re
from grammar import *

startshape_regex = re.compile(r"\s*startshape\s+(?P<startshapename>\w+)\n")
shape_regex = re.compile(r"\s*(?<!start)shape\s+(?P<shapename>\w+)")
single_rule_regex = re.compile(shape_regex.pattern + r"\s+(?P<ruleweight>[\d\-\.]*\s*)(?:\n\s*\{|\{)\n?(?:[^\}]*\n?)+\s*\}")
rule_regex = re.compile(r"\s*rule\s+(?P<ruleweight>[\d\-\.]*\s*)(?:\n\s*\{|\{)\n?(?:[^\}]*\n?)+\s*\}")

def grammar_from_file(filename):
	return grammar_from_string(read_file(filename))

def grammar_from_string(string):
	g = Grammar()

	# Extract startshape
	startshapematch = startshape_regex.search(string)
	if not startshapematch:
		print "Error: Could not find start shape"
		raise Exception

	g.startshape.name = startshapematch.groupdict()["startshapename"]


	# Extract all shapes and rules
	shapematches = list(shape_regex.finditer(string))
	for i in range(len(shapematches)):
		shapematch = shapematches[i]
		print "found shape at index: {0}".format(shapematch.groupdict())
		shape = Shape(shapematch.groupdict()["shapename"])
		g.shapes.append(shape)

		# Extract all rules for shape
		if i < len(shapematches) - 1:
			nextshapematch = shapematches[i+1]
			nextshapestart = nextshapematch.start()
		else:
			nextshapestart = len(string)

		nextruleindex = shapematch.start()
		singlerulematch = single_rule_regex.search(string, shapematch.start(), nextshapestart)
		if singlerulematch:
			# Shape has only one rule
			rulematches = [singlerulematch]
		else:
			rulematches = list(rule_regex.finditer(string, shapematch.end(), nextshapestart))

		# create rule for each match
		for match in rulematches:
			print "\tRule match found at index {0}".format(match.start())
			weightstr = match.groupdict()["ruleweight"]
			if weightstr == "":
				weight = 1.0
			else:
				weight = float(weightstr)
			rulebody = match.string
			rule = Rule(rulebody, weight)
			g.rules.append(rule)
			shape.rules.append(rule)


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
	#s = read_file("grammars/clouds.cfdg")
	#m = re.search(startshape_regex, s)
	#print m.groupdict()
