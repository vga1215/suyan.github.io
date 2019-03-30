def fab(max):
	a,b = 0,1
	while b < max:
		yield b
		a, b= b, a+b

for i in fab(234):
	print i, ",",
