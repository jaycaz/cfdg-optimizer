# Jordan Cazamias
# CFDG Optimizer
# June 2014

# test_save_exemplar.py: test generating an exemplar from a grammar and saving it to a file

import os

from cfdg_optimizer.exemplar import exgen
from cfdg_optimizer.grammar import gramparse
from cfdg_optimizer.utils import saveutils


def run_test():
    testgrammarfile = "flofree.cfdg"
    testdir = "test-save-exemplar"
    newfilename = "{0}/flofree.png".format(testdir)
    if not os.path.isdir(testdir):
        print "Creating directory {0}...".format(testdir)
        os.mkdir(testdir)

    # Create grammar
    print "Creating grammar from file '{0}'...".format(testgrammarfile)
    g = gramparse.grammar_from_file(testgrammarfile)

    print "Running CFDG with grammar body..."
    exemplar = exgen.generate_exemplar(g)

    print "Saving exemplar image to '{0}'...".format(
        saveutils.first_available_filename(newfilename))
    exemplar.save_image(newfilename)

    print "Exemplar successfully saved!"


if __name__ == "__main__":
    run_test()
