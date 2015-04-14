import sys
import random
import datetime




def sort_test (sort_func, input_number) :
	input = []
	for n in range(0, input_number) :
		input.append(random.randint(0,1000))
	print("input:\t" + str(input))
	start = datetime.datetime.today()
	output = sort_func(input) 
	end = datetime.datetime.today()
	print("output:\t" + str(output))
	print("time:\t" + str(end-start))

