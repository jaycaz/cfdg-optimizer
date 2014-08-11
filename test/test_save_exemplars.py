# Jordan Cazamias
# CFDG Optimizer
# June 2014

# test_save_exemplar.py: test generating an exemplar from a grammar and saving it to a file

import os
import shutil

from cfdg_optimizer.exemplar import exgen, exsave
from cfdg_optimizer.grammar import gramparse
from cfdg_optimizer.utils import saveutils


def run_test():
    numexemplars = 10
    testgrammarfile = "flofree.cfdg"
    testdir = "test-save-exemplars"
    savefilename = "{0}/flofree.png".format(testdir)
    if os.path.isdir(testdir):
        shutil.rmtree(testdir)
    print "Creating directory {0}...".format(testdir)
    os.mkdir(testdir)

    # Create grammar
    print "Creating grammar from file '{0}'...".format(testgrammarfile)
    g = gramparse.grammar_from_file(testgrammarfile)

    # Generate <numexemplars> exemplars
    print "Generating {0} exemplars...".format(numexemplars)
    exemplars = exgen.generate_exemplars(g, numexemplars, debug=True)
    assert len(exemplars) == numexemplars, \
        "Expected {0} exemplars to be generated, " \
        "instead have {1}".format(numexemplars, len(exemplars))

    # Saving exemplars to separate files
    print "Exemplars successfully generated. Saving exemplars to files..."
    for i, ex in list(enumerate(exemplars)):
        savefilename = saveutils.first_available_filename(savefilename)
        print "Saving exemplar {0} of {1} to {2}".format(i+1, numexemplars, savefilename)
        exsave.save_image(ex, savefilename)

    print "All exemplars successfully saved!"

if __name__ == "__main__":
    run_test()


