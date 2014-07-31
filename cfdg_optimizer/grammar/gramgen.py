# Jordan Cazamias
# CFDG Optimizer
# April 2014

# gramgen.py: Grammar Variant Generation

import copy
import math
import random as rand

from cfdg_optimizer.grammar import gramparse


MAX_WEIGHT = 100
INIT_STDDEV = 2


def gen_weight(center, std_dev):
    """
    Generates new weight using appropriate random distribution
    """
    r = rand.lognormvariate(math.log(center), std_dev)
    return min(r, MAX_WEIGHT)


def calc_stddev(roundnum, totalrounds):
    """
    Determines variation in randomness for variant generation

    :param roundnum: Current round number, out of totalrounds
    :param totalrounds: Total number of rounds in optimization
    """
    if roundnum == 1:
        return INIT_STDDEV
    s = INIT_STDDEV * (1 - (float(roundnum - 1) / totalrounds))
    return max(0, s)


def generate_variant(grammar, roundnum, totalrounds, seed=None):
    """
    Creates grammar variant using simulated annealing.
    Variation will decrease depending on roundnum / totalrounds
    """
    if seed:
        rand.seed(seed)

    # Copy grammar and alter rule weights
    newgrammar = copy.deepcopy(grammar)
    for rule in newgrammar.rules:
        if rule.fixed:
            continue

        # Update rule weight
        newweight = gen_weight(rule.weight, calc_stddev(roundnum, totalrounds))
        # print "{0} -> {1}".format(rule.weight, newweight)
        rule.weight = newweight

        # Update rule body string and overall grammar string with new weight
        # TODO: Change to avoid changing a different rule if two identical rules in the grammar
        rulematch = gramparse.rule_regex.search(rule.body)
        if rulematch is None:
            rulematch = gramparse.single_rule_regex.search(rule.body)

        newrulebody = "{0}{1}{2}".format(
            rule.body[:rulematch.start("ruleweight")],
            str(newweight),
            rule.body[rulematch.end("ruleweight"):])

        newgrammarbody = newgrammar.body.replace(rule.body, newrulebody)
        # print "***************\n{0} \n------->\n {1}\n****************".format(rule.body, newrulebody)

        rule.body = newrulebody
        newgrammar.body = newgrammarbody
    return newgrammar

