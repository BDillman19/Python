import re

file = open('regex_sum_832467.txt')

sum = 0
fileStr = file.read()

numbers = re.findall('[0-9]+', fileStr)

print(len(numbers))

for number in numbers:
    sum += int(number)

print(sum)