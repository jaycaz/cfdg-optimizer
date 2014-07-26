# Jordan Cazamias
# CFDG Optimizer
# July 2014

import cfdg_parser
import variant_gen
import exemplar_gen
import exemplar_scoring

NUM_VARIANTS = 5
NUM_ROUNDS = 5
NUM_EXEMPLARS = 10

# Main function (run using main CLI command)
# Optimizes grammar <grammar_filename> using
# images in test directory <test_images_dir>
def run(grammar_filename, test_image_dir, **kwargs):
    kwargs['maxshapes'] = 500000
    grammar = cfdg_parser.grammar_from_file(grammar_filename)
    best_variant = None
    best_variant_score = None
    best_variant_version = None

    # Main optimization loop
    for roundnum in range(NUM_ROUNDS):
        print "*** Optimization round {0} of {1}".format(roundnum+1, NUM_ROUNDS)
        variants = []
        scoremap = {}

        # Generate and score round variants
        for variantnum in range(NUM_VARIANTS):
            print "Creating variant {0} of {1}".format(variantnum+1, NUM_VARIANTS)
            variant = variant_gen.generate_variant(grammar, roundnum, NUM_ROUNDS)
            variants.append(variant)

            # Generate and score exemplars for every variant
            ex_scores = []
            for exemplarnum in range(NUM_EXEMPLARS):
                print "\tCreating exemplar {0}-{1}...".format(variantnum+1, exemplarnum+1)
                exemplar = exemplar_gen.generate_exemplar(variant, **kwargs)
                score = exemplar_scoring.score_exemplar(exemplar, test_image_dir)
                print "\t\tExemplar score: {0}".format(score)
                ex_scores.append(score)

            # Find compiled score for variant
            variant_score = exemplar_scoring.compile_scores(ex_scores)
            scoremap[variant] = variant_score
            "Variant {0} score: {1}".format(variantnum+1, variant_score)

        # Find best scoring variant
        if best_variant is None:
            best_variant = scoremap.keys()[0]
            best_variant_score = scoremap[best_variant]
            best_variant_version = "1-1"

        for index, variant in list(enumerate(scoremap.keys())):
            if scoremap[variant] > best_variant_score:
                best_variant = variant
                best_variant_score = scoremap[variant]
                best_variant_version = "{0}-{1}".format(roundnum+1, index+1)

        print "Current best variant: {0} (score {1})".format(
            best_variant_version, best_variant_score)


    print "Best overall variant: Variant {0} with a score of {1}".format(
        best_variant_version, best_variant_score)


if __name__ == "__main__":
    run("grammars/clouds.cfdg", "testclouds")