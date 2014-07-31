# Jordan Cazamias
# CFDG Optimizer
# April 2014

# saveutils: Saving Utilities

import os.path


def first_available_filename(tryname):
    """
    Starting with <rootpath>, finds an appropriate digit to append
    to avoid a filename collision

    return: Unique file name to save to
    """
    if not os.path.isfile(tryname):
        return tryname

    filepath, extension = os.path.splitext(tryname)

    # Check if file already has a number appended
    i = 1
    dashindex = filepath.rfind('-')
    if dashindex != -1:
        if dashindex != len(filepath) - 1 and filepath[dashindex+1:].isdigit():
            i = int(filepath[dashindex+1:])
            filepath = filepath[:dashindex]

    while True:
        filename = "{0}-{1}{2}".format(filepath, i, extension)
        if not os.path.isfile(filename):
            return filename
        i += 1
