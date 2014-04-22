# Jordan Cazamias
# CFDG Optimizer
# April 2014


class Rule:
	def __init__(self, body = "", weight = 1, fixed = True):
		self.body = body
		self.weight = weight
		self.fixed = fixed

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
		for shape in self.shapes: string += "\t\t{0} \n\t\t - {1} Rule{2}\n".format(
				repr(shape), len(shape.rules), "" if len(shape.rules) == 1 else "s")
		string += "\tTotal Rules: {0}\n".format(len(self.rules))
		string += "\tStartshape: {0}\n".format(self.startshape)
		string += "}"
		return string

