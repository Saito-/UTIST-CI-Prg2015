# coding: utf-8

'''
Q5.py
10進数を入力してローマ数字で表示する
入力は0より大きく4000より小さい
'''

# 記号を対応する数値に変換するディクショナリ
dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

'''
10進1桁数字をローマ数字に変換する関数
'''
def Dec_to_RomanNum_u(u):
	if u == 9:
		return 'XI'
	elif u >= 5:
		ans = 'V'
		u -= 5
		ans += 'I'*u
		return ans
	elif u == 4:
		return 'IV'
	else:
		return 'I'*u

'''
10進数の10の位をローマ数字に変換する関数
'''
def Dec_to_RomanNum_d(d):
	if d == 9:
		return 'XC'
	elif d >= 5:
		ans = 'L'
		d -= 5
		ans += 'X'*d
		return ans
	elif d == 4:
		return 'XL'
	else:
		return 'X'*d

'''
10進数の100の位をローマ数字に変換する関数
'''
def Dec_to_RomanNum_h(h):
	if h == 9:
		return 'CM'
	elif h >= 5:
		ans = 'D'
		h -= 5
		ans += 'C'*h
		return ans
	elif h == 4:
		return 'CD'
	else:
		return 'C'*h

'''
10進数の1000の位をローマ数字に変換する関数
'''
def Dec_to_RomanNum_t(t):
	return 'M' * t

'''
10進数をローマ数字に変換する関数
'''
def Dec_to_RomanNum(num):	
	t = Dec_to_RomanNum_t(int(num[0]))
	h = Dec_to_RomanNum_h(int(num[1]))
	d = Dec_to_RomanNum_d(int(num[2]))
	u = Dec_to_RomanNum_u(int(num[3]))
	return t + h + d + u

if __name__ == '__main__':
	num = raw_input().zfill(4)
	#print num
	print Dec_to_RomanNum(num)
