import math as mth
import numpy as num
import matplotlib.pyplot as plt

#################################################################################################
## 1.2-2 	サイズnの入力に対し各ソートのオーダーは、挿入ソートが8n^2、マージソートが64nlgn。
## 			マージソート＜挿入ソートとなる値を求めよ。

#挿入ソートのオーダー
def calc_insert_sort_order(n) : 
	return 8 * (n ** 2)
	
#マージソートのオーダー
def calc_merge_sort_order(n) :
	return 64 * n * mth.log(n, 2)

#比較。1は怪しい挙動なので２から。44が正解。
def compare_merge_and_insert() : 
	n = 2
	while calc_insert_sort_order(n) < calc_merge_sort_order(n) :
		n = n + 1
	return n

#xのリストに対してyのリストを作成
def create_ploty(func, x) : 
	return list(map (func, x))

#オーダーの増加を比較するグラフを描画。８０−１００くらいがきれいに見える。
def create_graphs_for_merge_and_insert(n) : 
	create_comparing_graphs(calc_insert_sort_order, calc_merge_sort_order, n)

def create_comparing_graphs(func1, func2, n) : 
	x = num.arange(1,n,1)
	y1 = create_ploty(func1, x)
	y2 = create_ploty(func2, x)
	plt.plot(x, y1)
	plt.plot(x, y2)
	plt.show()


#################################################################################################
## 1.2-3 	100 * (n**2) が 2**n　よりも高速になる最小のn。

# 1.2-2の描画関数を使ってグラフを見てみる。１７くらいがきれいに見える。
def create_graphs_for_123(n) :
	create_comparing_graphs((lambda x:(100 * (x**2))), (lambda x:(2**x)), n)

# 実際に比べてみる。lambdaの練習もかねる。15が正解。
def compare123() : 
	func1 = lambda x : 100 * (x**2)
	func2 = lambda x : 2**x
	n = 1
	while func1(n) > func2(n) : 
		n += 1
	return n


#################################################################################################
## 章末問題 1-1 	f(n)マイクロ秒（lg n, sqrt n, n, n lg n, n**2, n**3, 2**n, n!）で解けるアルゴリズムに対して、
##				１秒、１分、１時間、１日、１月、１年、１世紀に解けるサイズnを求める。				
##				1マイクロ秒は100万分の１秒

# 各時間をマイクロ秒で定義
sec = 1 * 1000000
minute = sec * 60
hour = minute * 60
day = hour * 24
month = day * 30
year = day * 365
century = year * 100

def calc_steps(func) :
	print("1秒 :\t" + str (func(sec)))
	print("1分 :\t" + str (func(minute)))
	print("1時間 :\t" + str (func(hour)))
	print("1日 :\t" + str (func(day)))
	print("1ヶ月 :\t" + str (func(month)))
	print("1年 :\t" + str (func(year)))
	print("1世紀 :\t" + str (func(century)))



## t秒で実行できるステップ数を求めるのでt = f(n)の逆関数を考える
## t = lg n -->	n = 2**t
def calc_lg_n() :
	calc_steps(lambda t : (2**t))
# 回答が帰ってこない。。

### t = sqrt n 	-->		n = t**2 (t >= 0) ###
def calc_sqrt_n() :
	calc_steps(lambda t : (t**2))

##　計算結果
## >>> c.calc_sqrt_n()
## 1秒 :		1000000000000
## 1分 :		3600000000000000
## 1時間 :	12960000000000000000
## 1日 :		7464960000000000000000
## 1ヶ月 :	6718464000000000000000000
## 1年 :		994519296000000000000000000
## 1世紀 :	9945192960000000000000000000000

### t = n --> n = t ###
def calc_n() : 
	calc_steps(lambda t : (t))

## 計算結果
## >>> c.calc_n()
## 1秒 :		1000000
## 1分 :		60000000
## 1時間 :	3600000000
## 1日 :		86400000000
## 1ヶ月 :	2592000000000
## 1年 :		31536000000000
## 1世紀 :	3153600000000000


### n lg n --> わからない。。。ので適当にオーダーをあげていく関数をつくる
def calc_by_actual(func) :
	tlist = [("秒",sec), ("分", minute), ("時間", hour), ("日", day), ("月", month), ("年", year), ("世紀", century)]
	n = 2
	t = tlist.pop(0)
	while n > 0 : 
		a = func(n)
		if a > t[1] : 
			print("1" + t[0] + " :\t" + str(n-1))
			if len(tlist) == 0 :
				break
			else :
				t = tlist.pop(0)
		n = n+mth.ceil(n*0.0001)

def calc_n_lg_n() :
	calc_by_actual(lambda n : (n * mth.log(n, 2)))

## 雑だけどこんな感じで。。。
## >>> c.calc_n_lg_n()
## 1秒 :		62748
## 1分 :		2801423
## 1時間 :	133390423
## 1日 :		2755253708
## 1月 :		71876417023
## 1年 :		797696293514
## 1世紀 :	68617660443872

### n**2 		--> 	sqrt n
def calc_n_square() :
	calc_steps(lambda t : mth.floor(mth.sqrt(t)))

## >>> c.calc_n_square()
## 1秒 :		1000
## 1分 :		7745
## 1時間 :	60000
## 1日 :		293938
## 1ヶ月 :	1609968
## 1年 :		5615692
## 1世紀 :	56156922

### n**3 --> n**(1/3)
def calc_n_cube() :
	calc_steps(lambda t : mth.floor(t**(1/3)))

## >>> c.calc_n_cube()
## 1秒 :		99
## 1分 :		391
## 1時間 :	1532
## 1日 :		4420
## 1ヶ月 :	13736
## 1年 :		31593
## 1世紀 :	146645

### 2**n --> lg n
def calc_nth_power_of_two() :
	calc_steps(lambda t : mth.floor(mth.log(t, 2)))

## >>> c.calc_nth_power_of_two()
## 1秒 :		19
## 1分 :		25
## 1時間 :	31
## 1日 :		36
## 1ヶ月 :	41
## 1年 :		44
## 1世紀 :	51

### n! --> これもわからないので実計算
def calc_n_factorial() :
	calc_by_actual(lambda n : mth.factorial(n))

## >>> c.calc_n_factorial()
## 1秒 :		9
## 1分 :		11
## 1時間 :	12
## 1日 :		13
## 1月 :		15
## 1年 :		16
## 1世紀 :	17

















