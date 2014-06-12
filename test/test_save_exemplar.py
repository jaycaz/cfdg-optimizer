# Jordan Cazamias
# CFDG Optimizer
# June 2014

# test_save_exemplar.py: test generating an exemplar from a grammar and saving it to a file

import os
import sys
sys.path.append("..")

import cfdg_parser as c
import exemplar_gen as egen
import save_utils as save


def run_test():
    testgrammarfile = "flofree.cfdg"
    testdir = "test-save-exemplar"
    newfilename = "{0}/flofree.png".format(testdir)
    if not os.path.isdir(testdir):
        print "Creating directory {0}...".format(testdir)
        os.mkdir(testdir)

    # Create grammar
    print "Creating grammar from file '{0}'...".format(testgrammarfile)
    g = c.grammar_from_file(testgrammarfile)

    print "Running CFDG with grammar body..."
    exemplar = egen.generate_exemplar(g)

    print "Saving exemplar image to '{0}'...".format(
        save.first_available_filename(newfilename))
    exemplar.save_image(newfilename)

    print "Exemplar successfully saved!"


if __name__ == "__main__":
    run_test()
