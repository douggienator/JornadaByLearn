def bigBang(i):
	if i % 3 == 0:
		if i % 5 == 0:
			print(f"{i} - BigBang!")
		else:
			print(f"{i} - Big")
	elif i % 5 == 0:
		print(f"{i} - Bang")
	else:
		print(i)

def listBigBang(i):
	for i in range(1, i + 1):
		bigBang(i)