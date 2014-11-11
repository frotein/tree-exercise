# takes in a list representation of a treeLevel and returns the list representation of the next level
def computeNextLevel(tree):
	lst = [] # the list being returned
	if len(tree)  == 1 : # if this is the beginning, return the second level
		lst.append(tree[0])
		lst.append(tree[0])
	else:
		i = 0
		while i < len(tree):

			if i == 0: # the left edge is always 1
				lst.append(1)
				lst.append(tree[i] + tree[i + 1])
			else:
				if i == (len(tree) - 1): # the right edge is always 1
					lst.append(tree[i - 1] + tree[i])
					lst.append(1)
				else: # computing middle is adding the values next to eachother
					lst.append(tree[i - 1] + tree[i])
					lst.append(tree[i] + tree[i + 1])

			i = i + 1
	return lst

# input the number of levels
levels = input("levels in tree: ")

# if the input is not a positive integer, retun an error
if not isinstance(levels , int) :
	print "Error: input is not a positive Integer"
else :
	if levels <= 0 :
		print "Error: input is not a positive Integer"
	else :
		# initialize tree as a list
	
		treeIn = [1]
		j = 1
		print treeIn
		while j < levels :
			treeIn = computeNextLevel(treeIn)
			print treeIn
			j = j + 1
	


