# Jordan Cazamias
# CFDG Optimizer
# April 2014

import os.path

# Starting with rootname, finds an appropriate digit to append
# to avoid a file collision
def first_available_filename(rootpath):
	if not os.path.isfile(rootpath):
		return rootpath

	if rootpath[-5:] == ".cfdg":
		strippath = rootpath[0:-5]
	else:
		strippath = rootpath
	i = 1
	while 1:
		filename = "{0}-{1}.cfdg".format(strippath, i)
		if not os.path.isfile(filename):
			return filename
		i += 1


# Writes out grammar contents to new file <outfilename>
# If <override> is true, it will write to <outfilename> without question
# If <override> is false, it will search for the first available filename
#    using first_available_filename
def save_grammar(grammar, outfilename, override = False):
	if override:
		usefilename = outfilename
	else:
		usefilename = first_available_filename(outfilename)

	f = open(usefilename, 'w')
	f.write(grammar.body)
	f.close()
