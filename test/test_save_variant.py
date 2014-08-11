# Jordan Cazamias
# CFDG Optimizer
# April 2014

# test_save_variant.py: test reading in grammar from file, creating a variant,
# and saving it to another file

import os

from cfdg_optimizer.grammar import gramgen, gramparse, gramsave
from cfdg_optimizer.utils import saveutils


g = None
v = None


def run_test():
    global g
    global v

    filename = "clouds.cfdg"
    dirname = "test-save-variant"
    newfilename = "{0}/test-save-variant.cfdg".format(dirname)
    if not os.path.isdir(dirname):
        print "Creating directory {0}...".format(dirname)
        os.mkdir(dirname)

    print "Reading grammar from file: " + filename + "..."
    g = gramparse.grammar_from_file(filename)

    print "Creating variant from grammar..."
    v = gramgen.generate_variant(g, 1, 5)

    print "Saving variant to file: " + \
          saveutils.first_available_filename(newfilename)
    gramsave.save(v, newfilename)

    print "Variant successfully saved!"

if __name__ == "__main__":
    run_test()

