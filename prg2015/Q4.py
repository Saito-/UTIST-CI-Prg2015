# coding: utf-8

'''
Q4.py
ローマ数字を入力して10進数で表示する
入力は0より大きく4000より小さい
'''

from collections import deque

# 記号を対応する数値に変換するディクショナリ
dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

'''
入力の先頭から連続する M の数を返す関数
'''
def cont_M(num):
	if num[0] != 'M': return 0
	num.popleft()
	ans = 1
	while len(num) != 0:
		if num[0] != 'M': break
		num.popleft()
		ans += 1
	return ans

'''
ローマ数字を10進数に変換する関数
1000の位の値は前処理 cont_M() により予め計算されているとする
計算の都合上 引数は deque として渡す
'''
def RomanNum_to_Dec(num):
	ans = 0
	while len(num) > 0:
		n = len(num)
		ch = num[n-1]
		if ch == 'X' and n >= 2:
			tmp = num[n-2]
			if tmp == 'I':
				ans += 9
				num.pop()
				num.pop()
			else:
				ans += 10
				num.pop()
		elif ch == 'V' and n >= 2:
			tmp = num[n-2]
			if tmp == 'I':
				ans += 4
				num.pop()
				num.pop()
			else:
				ans += 5
				num.pop()
		elif ch == 'C' and n >= 2:
			tmp = num[n-2]
			if tmp == 'X':
				ans += 90
				num.pop()
				num.pop()
			else:
				ans += 100
				num.pop()
		elif ch == 'L' and n >= 2:
			tmp = num[n-2]
			if tmp == 'X':
				ans += 40
				num.pop()
				num.pop()
			else:
				ans += 50
				num.pop()
		elif ch == 'M' and n >= 2:
			tmp = num[n-2]
			if tmp == 'C':
				ans += 900
				num.pop()
				num.pop()
			else:
				ans += 1000
				num.pop()
		elif ch == 'D' and n >= 2:
			tmp = num[n-2]
			if tmp == 'C':
				ans += 400
				num.pop()
				num.pop()
			else:
				ans += 500
				num.pop()
		else:
			ans += dic[num.pop()]
	return ans

if __name__ == '__main__':
	num = raw_input()
	d = deque(num)
	t = cont_M(d) * 1000
	n = RomanNum_to_Dec(d)
	print t + n
