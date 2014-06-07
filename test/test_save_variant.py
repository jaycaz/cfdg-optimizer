# Jordan Cazamias
# CFDG Optimizer
# April 2014

# test_save_variant.py: test reading in grammar from file, creating a variant,
# and saving it to another file

import os
import sys
sys.path.append("..")

import cfdg_parser as c
import variant_gen as vgen
import save_utils as save

g = None
v = None


def run_test():
    global g
    global v

    filename = "clouds.cfdg"
    dirname = "clouds-variants"
    newfilename = "{0}/test-save-variant.cfdg".format(dirname)
    if not os.path.isdir(dirname):
        print "Creating directory {0}...".format(dirname)
        os.mkdir(dirname)

    print "Reading grammar from file: " + filename + "..."
    g = c.grammar_from_file(filename)

    print "Creating variant from grammar..."
    v = vgen.generate_variant(g, 1, 5)

    print "Saving variant to file: " + save.first_available_filename(newfilename)
    save.save_grammar(v, newfilename)


if __name__ == "__main__":
    run_test()

