a=100000000
for x in range(1,9):
	if(x>=1 and x<=2):
		b=a*0
		print("laba bulan ke-",x," :",b)
	if(x>=3 and x<=4):
		c=a*0.01
		print("laba bulan ke-",x," :",c)
	if(x>=5 and x<=7):
		d=a*0.05
		print("laba bulan ke-",x," :",d)
	if(x==8):
		e=a*0.02
		print("laba bulan ke-",x," :",e)
total = b+b+c+c+d+d+d+e
print("\ntotal : ", total)