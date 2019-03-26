# Print every number from 1 to num
# if divisible by 3 print Fizz
# if divisible by 5 print Buzz
# else print the number

def FizzBuzz(num):
	for number in range(1, num):
		if number % 3 == 0:
			print("Fizz")
		elif number % 5 == 0:
			print("Buzz")
		else:
			print(number)