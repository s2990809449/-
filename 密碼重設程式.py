# 密碼重設程式
while True:
	password = 'a123456s'
	password = input('請輸入密碼: ')
	if password == 'a123456s':
		print('登入成功!')
		break
	else: 
		print('密碼錯誤 還有2次機會')
		while True:
			password = input('請輸入密碼: ')
			if password == 'a123456s':
				print('登入成功!')
				break
			else: 
				print('密碼錯誤 還有1次機會')
				while True:
					password = input('請輸入密碼: ')
					if password == 'a123456s':
						print('登入成功!')
						break
					else: 
						print('密碼錯誤 GG')
						break
				break
		break
		




