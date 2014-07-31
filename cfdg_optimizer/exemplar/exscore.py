# Jordan Cazamias
# CFDG Optimizer
# June 2014

# exscore.py: Exemplar Scoring

import os

from PIL import Image

from cfdg_optimizer.optimize import imgcomp


def score_exemplar(exemplar, test_image_dir):
    """
    Compares exemplar to all images in test_img_dir and computes score.

    :return: Overall exemplar score
    """
    individual_scores = []

    try:
        testfiles = os.listdir(test_image_dir)
    except OSError as e:
        print "Error: directory '{0}' could not be opened.".format(
            test_image_dir)
        raise e

    for filename in testfiles:
        try:
            test_image = Image.open("{0}/{1}".format(
                test_image_dir.rstrip('/'), filename))
        except IOError:
            continue

        image_score = imgcomp.compare(exemplar.image, test_image)
        individual_scores.append(image_score)

    if not individual_scores:
        raise Exception("ERROR: no files in {0} could be opened as images"
                        .format(test_image_dir))

    compiled_score = _compile_scores(individual_scores)
    return compiled_score

def _compile_scores(scores):
    """
    :param scores: list of scores for an exemplar
    :return: overall exemplar score
    """
    compiled_score = sum(scores) / len(scores)
    return compiled_score
