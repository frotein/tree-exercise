import sys

# If there are more or less than one input, return an error
if len(sys.argv) != 2 :
	print "Error : invalid number of inputs"
else :
	# otherwise, set input as a number 
	num = int(sys.argv[1])
	print num
