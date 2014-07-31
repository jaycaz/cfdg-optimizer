# Jordan Cazamias
# CFDG Optimizer
# July 2014

# gramscore.py: Grammar variant scoring

import os

from PIL import Image

from cfdg_optimizer.optimize import imgcomp


def score_grammar(exscores):
    """
    Compiles overall grammar score based on scores of its exemplars

    :param exscores: List of exemplar scores

    :return: Overall grammar score
    """

    compiled_score = sum(exscores) / len(exscores)
    return compiled_score
