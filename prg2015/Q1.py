# coding: utf-8

'''
Q1.py
4進数を入力して10進数で表示する
'''


'''
4のn乗を返す関数
'''
def pow_4(n):
	ret = 1
	for i in xrange(n):
		ret *= 4
	return ret

'''
4進数を10進数に変換する関数
 num: 入力4進数 (文字列)
'''
def conv4_to_10(num):
	n = len(num)
	ans = 0
	for i in xrange(n):
		ans += int(num[n-i-1])*pow_4(i)
	return ans

if __name__ == '__main__':
	num = raw_input()
	print conv4_to_10(num)
