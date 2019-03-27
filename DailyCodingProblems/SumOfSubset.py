# Given a list of integers S and a target number k,
# write a function that returns a subset of S that adds up to k.
# If such a subset cannot be made, then return null.

# Integers can appear more than once in the list.
# You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24,
# return [12, 9, 2, 1] since it sums up to 24.

def findSumOfSubset(allNumbers, targetValue):
	
	# If any numbers in the list of allNumbers is larger
	# than the targetValue, remove it since it will never
	# be used
	for number in allNumbers:
		if number > targetValue:
			allNumbers.remove(number)

	# This will hold the different possible permutations
	# of the allNumbers list
	perms = [[]]

	# find a possible permutation and for each one check
	# if the temporary sum equals our sum above
	# if found return the temporary list
	for i in range(0, len(allNumbers)):
		perms_len = len(perms)
		for j in range(0, perms_len):
			temp = perms[j] + [allNumbers[i]]
			perms.append(temp)
			if sum(temp) == targetValue:
				print(temp)
				return temp

	return None

# This unit tests runs findSumOfSubset with the example
# data above.
def testSumOfSubset():
	assert findSumOfSubset([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]

if __name__ == "__main__":
	testSumOfSubset()
	print("sum of Subsets works correctly")