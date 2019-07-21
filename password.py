x = 0
while x < 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('錯誤')
		x = x + 1
