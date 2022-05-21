# 密碼重設程式
password = 'a123456s'
i = 3
while i > 0:
	i = i - 1
	pws = input('請輸入密碼: ')
	if pws == password:
		print('登入成功')
		break
	else:
		if i > 0:
			print('密碼錯誤 你還有', i, '次機會')
		else:
			print('登入失敗')

		


