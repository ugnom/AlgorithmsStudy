import sys
from enum import IntEnum

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
初期条件：		空の配列には、vの値は入っていない
ループ内条件：	0から(i-1)までの配列にv入っていないとするとき、[i]==vだとすると終了。
			そうでない場合、[i]はvでないので0からiまでの配列にvが入っていないと保証できる。
終了条件：		配列内のすべての値をチェックするとループ終了。結果はNIL(-1)を返す。
'''

## 2.1-4 	二つのn要素配列AとBに蓄えられた2つのnビットの2進数の輪を求める。
##			(n+1)要素配列Cに和を蓄える。
# 二進数型
class Bin(IntEnum) :
	l = 1
	o = 0

def binary_add(a, b) :
	c = []
	carry = Bin.o
	for i in reversed(range(len(a))) :
		#１の本数で該当ビットの値とキャリーをパターンわけする
		l_count = a[i] + b[i] + carry
		if l_count == 0 :
			c.insert(0, Bin.o)
			carry = Bin.o
		elif l_count == 1 :
			c.insert(0, Bin.l)
			carry = Bin.o
		elif l_count == 2 :
			c.insert(0, Bin.o)
			carry = Bin.l
		else :
			c.insert(0, Bin.l)
			carry = Bin.l
	c.insert(0, carry)
	return c

'''
>>> l = c.Bin.l
>>> o = c.Bin.o

>>> a = [o,o,o,o,l,l,l,l]
>>> b = [o,o,l,l,o,o,o,l]
>>> c.binary_add(a, b)
[<Bin.o: 0>, <Bin.o: 0>, <Bin.l: 1>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>]

>>> a = [l,l,l,l,l,l,l,l]
>>> b = [o,o,o,o,o,o,o,l]
>>> c.binary_add(a, b)
[<Bin.l: 1>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>, <Bin.o: 0>]
'''

################################################################################

## 2.2-1　(n**3) / 1000 - 100(n**2) - 100n + 3をΘで表現
'''
n**2以下の項については丸められるため、Θ(n**3)といえる
'''

## 2.2-2 選択ソートを実装する。

## 選択ソート
def select_sort(input) :
	output = input
	for i in range(len(output)-1) :
		minimum = output[i]
		min_index = i
		for j in range(i, len(output)) :
			if minimum > output[j] :
				minimum = output[j]
				min_index = j
		output[min_index] = output[i]
		output[i] = minimum
	return output

'''
>>> c2.select_sort([8,3,5,7,4,2,9,1])
[1, 2, 3, 4, 5, 7, 8, 9]
'''
'''
ループ不変式：
不変条件：		0からiまでの項についてソートが完了している
初期条件：		0から0まですなわち空のリストについては自明
ループ内条件：	0から(i-1)までソートが完了していると仮定する。ループ内では残りのリストの中の最小値を探索し、最終的に[i]の値と交換する。
			iからリストの最後には、必ず0から(i-1)までの値よりも大きい値しか入っていないので、0からiまでのソートが完了したといえる。
終了条件：		i=(n-1)までを捜査して終了。このときn-1までのソートが完了しており、[n]には最大の値が入っているため、nの捜査はする必要がない

'''

## 2.2-3 順次探索法（2.1-3)の平均実行時間と最悪実行時間について
'''
平均実行時間：n/2 --> Θ(n)
実際の実行時間は、vにマッチする値の場所に依存するため、
				確率		実行時間
[0]に存在する：		100/n　	1
[1]に存在する：		100/n 	2
...
[n-2]に存在する：	100/n 	n-1
[n-1]に存在する：	100/n 	n
つまり実行時間の期待値はおおよそ、
((100/n * 1) + (100/n * 2)+ ... (100/n * (n-1)) + (100/n * (n))) / n = n/2

最悪実行時間
最悪実行時間は、vが(n-1)に存在するときなので、nとなる
'''


################################################################################
## マージソート 番兵付き

def merge_sort (input, logging=False) : 
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
			if(logging == True) :
				print("LEFT:\t" + str(input[p:q+1]))
			merge_sort_loop (input, q+1, r)
			if(logging == True) :
				print("RIGHT:\t" + str(input[q+1:r+1]))
			merge (input, p, q, r)
		
	output = input 
	merge_sort_loop (output, 0, len(output)-1)

	return output


################################################################################
## 2.3-1 [3,41,52,26,38,57,9,49]のソート
'''
>>> c2.merge_sort([3,41,52,26,38,57,9,49], True)
LEFT:   [3]
RIGHT:  [41]
LEFT:   [3, 41]
LEFT:   [52]
RIGHT:  [26]
RIGHT:  [26, 52]
LEFT:   [3, 26, 41, 52]
LEFT:   [38]
RIGHT:  [57]
LEFT:   [38, 57]
LEFT:   [9]
RIGHT:  [49]
RIGHT:  [9, 49]
RIGHT:  [9, 38, 49, 57]
[3, 9, 26, 38, 41, 49, 52, 57]
'''

## 2.3-2 マージソート 番兵なし
def merge_sort2 (input, logging=False) : 
	# defining recursive function internally used for separation of input
	def merge_sort_loop (input, p, r) : 
		# defining merge function internally used to sort the small sets
		def merge (input, p, q, r) :
			left = input[p:q+1]
			right = input[q+1:r+1]
			i = 0
			j = 0
			for k in range(p, r+1) :
				if left[i] <= right[j] :
					input[k] = left[i]
					i = i + 1
				elif left[i] > right[j] :
					input[k] = right[j]
					j = j + 1
				#leftかrightが終わったら違うほうを差し込む
				if (i >= len(left) ) :
					if logging == True :
						print("left is done, putting :" + str(right[j:len(right)]))
					for l in range(k+1, r+1) :
						input[l] = right[j]
						j = j + 1
					break;
				elif(j >= len(right)) :
					if logging == True :
						print("right is done, putting :" + str(left[i:len(left)]))
					for l in range(k+1, r+1) :
						input[l] = left[i]
						i = i+1
					break;
		if p < r :
			q = int((p + r) / 2)
			merge_sort_loop (input, p, q)
			if(logging == True) :
				print("LEFT:\t" + str(input[p:q+1]))
			merge_sort_loop (input, q+1, r)
			if(logging == True) :
				print("RIGHT:\t" + str(input[q+1:r+1]))
			merge (input, p, q, r)
		
	output = input 
	merge_sort_loop (output, 0, len(output)-1)

	return output

'''
2.3-3 nが2のべき乗のとき、以下の漸化式の解がT(n) = n lg nであることを数学的帰納法を用いて示せ。 
	T(n) = 	{ 2 			n = 2のとき
			{ 2T(n/2) + n 	k > 1に対してn = 2**kのとき

	n = 2のとき、 2 lg 2 = 2なので確かにT(n)を満たす
	T(2**k) = T(n) がn lg nを満たすと仮定すると、T(2**(k+1)) = T(2n)は、

	T(2n) = 2T(n) + n
		  = 2(n lg n) + 2n
		  = lg (n**2n) + lg (2**2n)
		  = lg ((n**2n) * (2**2n))
		  = lg (2n**2n)
		  = 2n lg 2n
	よってnのとき条件を満たすと仮定すると2nも条件を満たす。

	数学的帰納法より、すべてのn = 2**kに対して漸化式が成り立つことが示された。
'''

## 2.3-4 挿入ソートの再帰版

def r_insertion_sort (input, logging=False, comp=compare_gt) :
	def sort_loop(input, j) :
		if j > 0 :
			sort_loop(input, j-1)
		key = input[j]
		i = j - 1
		while (i >= 0) & comp(input[i] , key)  : 
			input[i + 1] = input[i]
			i = i - 1
		input[i+1] = key

	output = input
	sort_loop(output, len(output)-1)
	return output

'''
T(n) = 	{ Θ(1) 				n=1のとき
		{ T(n-1) + O(n)		その他
'''

##2.3-5 ソート済みの配列に対して２分探索をする
def binary_search (sorted_input, v) :
	def search_loop(input, p, r, v) :
		if p == r :
			if input[p] == v :
				return p
			else :
				return -1
		q = int((p + r) / 2)
		if input[q] >= v :
			return search_loop(input, p, q, v)
		elif input[q] < v :
			return search_loop(input, q+1, r, v)
	return search_loop(sorted_input, 0, len(sorted_input)-1, v)

'''
２分探索
T(n) = 	{ 1 			n = 1
		{ T(n/2) + 1 	n >= 2

'''

##2.3-7 整数の集合から２個を取ってxと等しくなるものが存在するかを決定する。θ(n lg n)でよろしく。
def create_list_without (input, i) :
	out = list(input) 
	out.pop(i)
	return out

def sum_search (input, x) :
	#まずソートしてみる
	result = False
	sorted_list = merge_sort(input) 
	#多分θ(n lg n)
	for i in range(len(sorted_list)) :
		i_list = create_list_without(input, i)
		r = binary_search(i_list, (x-sorted_list[i]))
		print("i=" + str(i) + " i_list=" + str(i_list) + " r=" + str(r))
		if r == -1 : 
			continue
		else :
			result = True
			break
	return result


### 章末問題 ###
## 2-1 
'''
a. 
b.
c.
d.
'''















