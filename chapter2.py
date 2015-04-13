import sys

################################################################################
## 挿入ソート Logging オプション付き

def compare_gt (a, b) :
	return a > b

def compare_lt (a, b) :
	return a < b

def insertion_sort (input, logging=False, comp=compare_gt) :
	output = input 
	for j in range(len(output)) :
		key = output[j]
		i = j - 1
		if logging == True : 
			print(str(input) + " j=" + str(j) + " key=" + str(key))
		while (i >= 0) & comp(output[i] , key)  : 
			if logging == True : 
				sys.stdout.write("\t" + str(input))
			output[i + 1] = output[i]
			if logging == True : 
				print(" --> " + str(input) + "[(i+1)=" + str(i+1) + "] <- [i]=" + str(output[i]))
			i = i - 1
		if logging == True : 
			sys.stdout.write("\t" + str(input))
		output[i+1] = key
		if logging == True : 
			print(" --> " + str(input) + "[(i+1)=" + str(i+1) + "] <- key=" + str(key))

		
	return output

################################################################################
## リニアサーチ : 該当しない場合は-1を返す

def linear_search (input, v) :
	result = -1
	#０個のインプットにvの値はない
	assert(result == -1)
	for i in range(len(input)) :
		if v == input[i] :
			result = i
			break;
		#ループが回っているということはまだ見つかっていない
		assert(result == -1)
	#終了時には-1かindexのどちらかがはいる
	return result



## 2.1-1 配列 [31,41,59,26,41,58] のソートの様
'''
>>> c.insertion_sort([31,41,59,26,41,58], True)
[31, 41, 59, 26, 41, 58] j=0 key=31
	[31, 41, 59, 26, 41, 58] --> [31, 41, 59, 26, 41, 58][(i+1)=0] <- key=31
[31, 41, 59, 26, 41, 58] j=1 key=41
	[31, 41, 59, 26, 41, 58] --> [31, 41, 59, 26, 41, 58][(i+1)=1] <- key=41
[31, 41, 59, 26, 41, 58] j=2 key=59
	[31, 41, 59, 26, 41, 58] --> [31, 41, 59, 26, 41, 58][(i+1)=2] <- key=59
[31, 41, 59, 26, 41, 58] j=3 key=26
	[31, 41, 59, 26, 41, 58] --> [31, 41, 59, 59, 41, 58][(i+1)=3] <- [i]=59
	[31, 41, 59, 59, 41, 58] --> [31, 41, 41, 59, 41, 58][(i+1)=2] <- [i]=41
	[31, 41, 41, 59, 41, 58] --> [31, 31, 41, 59, 41, 58][(i+1)=1] <- [i]=31
	[31, 31, 41, 59, 41, 58] --> [26, 31, 41, 59, 41, 58][(i+1)=0] <- key=26
[26, 31, 41, 59, 41, 58] j=4 key=41
	[26, 31, 41, 59, 41, 58] --> [26, 31, 41, 59, 59, 58][(i+1)=4] <- [i]=59
	[26, 31, 41, 59, 59, 58] --> [26, 31, 41, 41, 59, 58][(i+1)=3] <- key=41
[26, 31, 41, 41, 59, 58] j=5 key=58
	[26, 31, 41, 41, 59, 58] --> [26, 31, 41, 41, 59, 59][(i+1)=5] <- [i]=59
	[26, 31, 41, 41, 59, 59] --> [26, 31, 41, 41, 58, 59][(i+1)=4] <- key=58
[26, 31, 41, 41, 58, 59]
'''

## 2.1-2 降順でのソートは、compare_lt関数を使って行う
'''
>>> c.insertion_sort([31,41,59,26,41,58], False, c.compare_lt)
[59, 58, 41, 41, 31, 26]
'''

## 2.1-3 リニアサーチのループ不変式

'''
>>> c.linear_search([1,2,3,4,5,6,7], 3)
2
>>> c.linear_search([1,2,3,4,5,6,7], 9)
-1
'''

'''
初期条件：	空の配列には、vの値は入っていない
ループ内条件：0から(i-1)までの配列にv入っていないとするとき、[i]==vだとすると終了。
			[i]はvでないので0からiまでの配列にvが入っていないと保証できる。
終了条件：	配列内のすべての値をチェックするとループ終了。結果はNILを返す。
'''


################################################################################
## マージソート

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
		if p < r :
			q = int((p + r) / 2)
			merge_sort_loop (input, p, q)
			merge_sort_loop (input, q+1, r)
			merge (input, p, q, r)
		
	output = input 
	merge_sort_loop (output, 0, len(output)-1)

	return output


