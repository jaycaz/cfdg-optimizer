# Jordan Cazamias
# August 2014
# CFDG Optimizer

# gramsave: utilities for saving grammars

from cfdg_optimizer.grammar import gramparse
from cfdg_optimizer.utils import saveutils

def save(grammar, tryfilename, override=False, clean=True):
    """
    Tries to write out grammar contents to new file <tryfilename>

    :param override:
        If <override> is true, it will write to <tryfilename> without question
        If <override> is false, it will search for the first available filename
        using first_available_filename

    :param clean: Determines whether the marked up grammar body
    or the cleaned up grammar body is saved

    :return: If successful, actual file name used
    """
    if override:
        usefilename = tryfilename
    else:
        usefilename = saveutils.first_available_filename(tryfilename)

    try:
        f = open(usefilename, 'w')
        if clean:
            f.write(gramparse.clean_body(grammar))
        else:
            f.write(grammar.body)
        f.close()
    except IOError as e:
        print "Error saving grammar '{0}' to {1}".format(
            grammar.name, usefilename)
        raise e

    return usefilename
