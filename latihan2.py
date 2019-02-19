max = 0
while True:
	a=int(input ("masukan bilangan : "))
	if max < int(a):
		max = int(a)
	if a == 0:
		break
print("bilangan terbesar", max)
