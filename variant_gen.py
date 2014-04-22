# Jordan Cazamias
# CFDG Optimizer
# April 2014

import copy
import math
import random as rand

from grammar import *

MAX_WEIGHT = 100
INIT_STDDEV = 2

# Generates new weight using appropriate random distribution
def gen_weight(center, std_dev):
	r = rand.lognormvariate(math.log(center), std_dev)
	return min(r, MAX_WEIGHT)

# Determines variation in randomness for variant generation
def calc_stddev(roundnum, totalrounds):
	if roundnum == 1:
		return INIT_STDDEV
	s = INIT_STDDEV * (1 - (float(roundnum - 1) / (totalrounds)))
	return max(0, s)

# Creates grammar variant using simulated annealing
# Variation will decrease depending on roundnum / totalrounds
def generate_variant(grammar, roundnum, totalrounds, seed = None):
	if seed != None:
		rand.seed(seed)

	newgrammar = copy.deepcopy(grammar)
	for rule in newgrammar.rules:
		if rule.fixed:
			continue
		oldweight = rule.weight
		rule.weight = gen_weight(oldweight, calc_stddev(roundnum, totalrounds))
		print "{0} -> {1}".format(oldweight, rule.weight)

	return newgrammar

def print_weights(grammar):
	weights = [rule.weight for rule in grammar.rules]
	print weights
