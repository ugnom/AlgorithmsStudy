import sys


#最大部分配列を求める
def find_maximum_subarray(input) : 
	def find_max_subarray_loop(input, low, high) : 
		def find_max_crossing_subarray(input, low, mid, high) : 
			left_sum = sys.maxsize * (-1)
			sum = 0
			max_left = mid
			for i in range(mid, (low - 1), -1) : 
				sum = sum + input[i]
				if sum > left_sum :
					left_sum = sum
					max_left = i
			right_sum = sys.maxsize * (-1)
			sum = 0
			max_right = mid + 1
			for j in range(mid + 1, high + 1) : 
				sum = sum + input[j]
				if sum > right_sum :
					right_sum = sum
					max_right = j
			return (max_left, max_right, left_sum + right_sum)
		if high == low : 
			return (low, high, input[low])
		else : 
			mid = int((low + high) / 2)
			(left_low, left_high, left_sum) = find_max_subarray_loop(input, low, mid)
			(right_low, right_high, right_sum) = find_max_subarray_loop(input, mid + 1, high)
			(cross_low, cross_high, cross_sum) = find_max_crossing_subarray(input, low, mid, high)
			if left_sum >= right_sum & left_sum >= cross_sum : 
				return (left_low, left_high, left_sum)
			elif right_sum >= left_sum & right_sum >= cross_sum : 
				return (right_low, right_high, right_sum)
			else : 
				return (cross_low, cross_high, cross_sum)
	output = input
	return find_max_subarray_loop(output, 0, len(output) - 1)

