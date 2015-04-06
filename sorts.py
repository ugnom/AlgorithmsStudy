import sys
import random
import datetime

def insertion_sort (input) :
	output = input 
	for j in range(len(output)) :
		key = output[j]
#		print ("j=" + str(j) + " key=" + str(key))
		i = j - 1
		while (i >= 0) & (output[i] > key)  : 
#			print ("  i=" + str(i) + " output[i]=" + str(output[i]))
			output[i + 1] = output[i]
			i = i - 1
		output[i+1] = key
	return output

def merge_sort (input) : 
	# defining recursive function internally used for separation of input
	def merge_sort_loop (input, p, r) : 
		# defining merge function internally used to sort the small sets
		def merge (input, p, q, r) :
			left = input[p:q+1] + [sys.maxsize]
			right = input[q+1:r+1] + [sys.maxsize]
			i = 0
			j = 0
			for k in range(p, r+1) :
				if left[i] <= right[j] :
					input[k] = left[i]
					i = i + 1
				elif left[i] > right[j] :
					input[k] = right[j]
					j = j + 1
			#print("sorted input:" + str(input))

		if p < r :
			q = int((p + r) / 2)
			merge_sort_loop (input, p, q)
			merge_sort_loop (input, q+1, r)
			merge (input, p, q, r)
		
	output = input 
	merge_sort_loop (output, 0, len(output)-1)

	return output





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

