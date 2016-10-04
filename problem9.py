import math
def run():
	a = 3
	b = 4
	
	while(a<1000):
		c = a ** 2 + b**2 
		if math.sqrt(c) == int(math.sqrt(c)):
			if(a+b+math.sqrt(c)==1000):
				print a*b*math.sqrt(c)
		if(b<1000):
			b = b+1
		else:
			a = a+1
			b=a

run()
