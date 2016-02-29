# coding: utf-8

'''
Q2.py
a ~ h までの記号で表された8進数を10進数で表示する
'''

# 記号を対応する数値に変換するディクショナリ
dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}


'''
8のn乗を返す関数
'''
def pow_8(n):
	ret = 1
	for i in xrange(n):
		ret *= 8
	return ret

'''
8進数を10進数に変換する関数
 num: 入力8進数 (文字列)
'''
def conv8_to_10(num):
	n = len(num)
	ans = 0
	for i in xrange(n):
		ans += dic[num[n-i-1]]*pow_8(i)
	return ans

if __name__ == '__main__':
	num = raw_input()
	print conv8_to_10(num)
