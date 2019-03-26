# implementing a job scheduler that takes in  a function and an integer
# and calls the function after n milliseconds

import time

def scheduler(myFunction, interval) :
	interval = interval/100
	print(interval)
	time.sleep(interval)

	myFunction

def aFunction() :
	print ("hello")