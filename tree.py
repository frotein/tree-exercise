#tree class, has a value, left and right nodes, and a link to its parent
class branch:
	def __init__(value, parent):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent

	def addLeft(tree):
		self.left = tree

	def addRight(tree):
		self.right = tree


# input the number of levels
levels = input("levels in tree: ")

# if the input is not a positive integer, retun an error
if not isinstance(levels , int) :
	print "Error: input is not a positive Integer"
else :
	if levels < 0 :
		print "Error: input is not a positive Integer"
	


