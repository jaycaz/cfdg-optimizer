# Jordan Cazamias
# CFDG Optimizer
# June 2014

# test_save_exemplar.py: test generating an exemplar from a grammar and saving it to a file

import os
import shutil
import sys
sys.path.append("..")

import cfdg_parser as c
import exemplar_gen as egen
import save_utils as save


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
    g = c.grammar_from_file(testgrammarfile)

    # Generate <numexemplars> exemplars
    print "Generating {0} exemplars...".format(numexemplars)
    exemplars = egen.generate_exemplars(g, numexemplars, debug=True)
    assert len(exemplars) == numexemplars, \
        "Expected {0} exemplars to be generated, " \
        "instead have {1}".format(numexemplars, len(exemplars))

    # Saving exemplars to separate files
    print "Exemplars successfully generated. Saving exemplars to files..."
    for i, ex in list(enumerate(exemplars)):
        savefilename = save.first_available_filename(savefilename)
        print "Saving exemplar {0} of {1} to {2}".format(i+1, numexemplars, savefilename)
        ex.save_image(savefilename)

    print "All exemplars successfully saved!"

if __name__ == "__main__":
    run_test()


