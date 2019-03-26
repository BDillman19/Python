# adds two binary numbers

def AddBinaryNumber(a, b):
	a = convertToDecimal(a)
	b = convertToDecimal(b)

	print(str(bin(a + b))[2:])

def convertToDecimal(binaryNumber):
	binaryNumberStr = str(binaryNumber)
	binList = list(binaryNumberStr)

	multiplier = len(binList) - 1
	entryInList = 0
	runningTotal = 0

	while multiplier >= 0:
		runningTotal = runningTotal + int(binList[entryInList]) * 2 ** multiplier
		multiplier = multiplier - 1
		entryInList = entryInList + 1

	return runningTotal
