# 密碼重設程式
password = 'a123456s'
i = 3
while True:
	pws = input('請輸入密碼: ')
	if pws == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤 你還有', i, '次機會')
	if i == 0:
		break
		


