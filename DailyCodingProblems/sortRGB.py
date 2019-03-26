# Given an array of strictly the characters 'R', 'G', and 'B',
# segregate the values of the array so that all the Rs come first,
# the Gs come second, and the Bs come last. You can only swap
# elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
#  it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']

currentEntry = 0
movedToFront = 0
movedToBack = 1

def sortRGB(rgbArray = ['G', 'B', 'R', 'R', 'B', 'B', 'R', 'G']):
	while currentEntry < len(rgbArray):
		print(currentEntry)
		print(rgbArray[currentEntry])
		if rgbArray[currentEntry] == 'B':
			moveEntryToBack(rgbArray, rgbArray[currentEntry])
		elif rgbArray[currentEntry] == 'R':
			entryMoveBack, entrySwap = currentEntry, movedToFront
			rgbArray[entryMoveBack], rgbArray[entrySwap] = rgbArray[entrySwap], rgbArray[entryMoveBack]
			movedToFront += 1

	sortRGB(rgbArray)

def moveEntryToBack(rgbArray, entry):
	entryMoveBack, entrySwap = entry, len(rgbArray) - movedToBack
	rgbArray[entryMoveBack], rgbArray[entrySwap] = rgbArray[entrySwap], rgbArray[entryMoveBack]
	movedToBack += 1
