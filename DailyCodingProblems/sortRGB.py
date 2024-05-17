# Given an array of strictly the characters 'R', 'G', and 'B',
# segregate the values of the array so that all the Rs come first,
# the Gs come second, and the Bs come last. You can only swap
# elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'B', 'R', 'G'],
#  it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B', 'B']

# Define variables
entry = 0
movedToFront = 0
movedToBack = 1
entriesMoved = 0

# used to track G entries that do not get moved to front or back
# without this the entriesMoved may get double counted
floatingEntries = {}

# Function to parse array
def sortRGB(rgbArray = ['G', 'B', 'R', 'R', 'B', 'B', 'R', 'G', 'B', 'R', 'G', 'G', 'B', 'B', 'R']):
	global entry, entriesMoved, floatingEntries

	print('inital : ', rgbArray)

	# while the entries moved to front or back AND G's is less than the length of the array
	while entriesMoved + len(floatingEntries) < len(rgbArray):
		if rgbArray[entry] == 'R':
			moveEntryToFront(rgbArray)
		elif rgbArray[entry] == 'B':
			moveEntryToBack(rgbArray)
		else:
			if entry in floatingEntries.keys():
				# do nothing entry has already been tracked
				return
			else:
				floatingEntries[entry] = rgbArray[entry]

		entry += 1

	print('result : ', rgbArray)

# Function to move value to end of array
def moveEntryToFront(rgbArray):
	global entry, movedToFront, entriesMoved, floatingEntries

	rgbArray[entry], rgbArray[movedToFront] = rgbArray[movedToFront], rgbArray[entry]
	entriesMoved += 1
	movedToFront += 1

	if entriesMoved + len(floatingEntries) >= len(rgbArray):
		return
	elif rgbArray[entry] == 'B':
		moveEntryToBack(rgbArray)
	elif rgbArray[entry] == 'R':
		moveEntryToFront(rgbArray)
	else:
		if movedToFront - 1 in floatingEntries.keys():
				# update dictionary with new location
				floatingEntries.pop(movedToFront - 1)
				floatingEntries[entry] = rgbArray[entry]
		else:
			floatingEntries[entry] = rgbArray[entry]

# Function to move value to beginning of array
def moveEntryToBack(rgbArray):
	global entry, movedToBack, entriesMoved, floatingEntries

	rgbArray[entry], rgbArray[len(rgbArray) - movedToBack] = rgbArray[len(rgbArray) - movedToBack], rgbArray[entry]
	entriesMoved += 1
	movedToBack += 1

	if entriesMoved + len(floatingEntries) >= len(rgbArray):
		return
	elif rgbArray[entry] == 'B':
		moveEntryToBack(rgbArray)
	elif rgbArray[entry] == 'R':
		moveEntryToFront(rgbArray)
	else:
		if len(rgbArray) - movedToBack - 1  in floatingEntries.keys():
				# update dictionary with new location
				floatingEntries.pop(len(rgbArray) - movedToBack - 1)
				floatingEntries[entry] = rgbArray[entry]
		else:
			floatingEntries[entry] = rgbArray[entry]

if __name__ == "__main__":
	sortRGB()