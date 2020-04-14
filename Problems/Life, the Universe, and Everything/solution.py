while(True):
	try:
		num = input()
	except (ValueError):
		break
	if(num == '42'):
			break
	else:
		print(num)
