# Jordan Cazamias
# CFDG Optimizer
# April 2014


class Rule:
	def __init__(self, body = "", weight = 1, isfixed = True):
		self.body = body
		self.weight = weight
		self.isfixed = isfixed

class Shape:
	def __init__(self, name = ""):
		self.name = name
		self.rules = []

	def __repr__(self):
		return "<Shape '{0}'>".format(self.name)

class Grammar:
	def __init__(self, shapes = [], rules = [], startshape = Shape()):
		self.shapes = shapes
		self.rules = rules
		self.startshape = startshape

	def __repr__(self):
		string = "Grammar \n{\n"
		string += "\tShapes:\n"
		shapenames = [repr(shape) for shape in self.shapes]
		for name in shapenames: string += "\t\t{0}\n".format(name)
		string += "\tRules: {0}\n".format(len(self.rules))
		string += "\tStartshape: {0}\n".format(self.startshape)
		string += "}"
		return string

