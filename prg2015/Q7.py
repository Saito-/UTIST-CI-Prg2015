# coding: utf-8

'''
Q7.py
英語で表記された数を10進数で表示する
入力は 100,000 より小さい 正の整数 (1 ~ 99,999)
'''

from collections import deque

# 文字列を対応する数値に変換するディクショナリ
dic = { 
	'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
	'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 
	'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15,
	'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
	'thirty':30, 'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90,
	'hundred':100, 'thousand':1000
}

'''
英語で表記された数を10進数に変換する関数
計算の都合上 引数は deque で受け取る
'''
def str_to_dec(nums):
	t = 0
	h = 0
	n = 0
	
	if len(nums) == 1:
		return dic[nums.popleft()]
	if 'thousand' in nums:
		while True:
			if nums[0] == 'thousand':
				nums.popleft()
				break
			t += dic[nums.popleft()]
	if 'hundred' in nums:
		while True:
			if nums[0] == 'hundred':
				nums.popleft()
				break
			h += dic[nums.popleft()]
	while len(nums) != 0:
		n += dic[nums.popleft()]
	return t*1000 + h*100 + n

if __name__ == '__main__':
	s = raw_input()
	#s = 'fifty four thousand three hundred twelve'
	#s = 'twelve hundred'
	nums = s.split()
	#print nums
	print str_to_dec(deque(nums))

