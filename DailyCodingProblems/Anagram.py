# Given an array of strings, return all groups of strings that are
# anagrams

# input ["bat", "tab", "car"]
# output ["bat", "tab"]

def findAnagrams(listOfStrings):
	splitStringsList = []
	resultList = []

	for string in listOfStrings:
		splitStringsList.append(list(string).sort())
	print(splitStringsList)
	for splitString in splitStringsList:
		entry = splitStringsList.index(splitString) + 1
	
		while entry < len(splitStringsList):
			if splitStringsList[entry] == splitString:
				resultList.append(listOfStrings[entry])
				resultList.append(listOfStrings[splitStringsList.index(splitString)])
			entry = entry + 1

	print(resultList)