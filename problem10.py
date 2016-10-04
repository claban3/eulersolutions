import math
def run():
	print sum(primes(2000000))
def primes(num):
	primes = []
	for i in range(num+1):
		primes.append(True)

	for j in range(2, int(math.ceil(math.sqrt(num)))):
		if primes[j] == True:
			x = 0
			k =(j ** 2) + (j * x)
			while k < len(primes):
				primes[k] = False
				x = x+1
				k = (j ** 2) + (j * x)

	primeNums = []

	for i in range(2, num):
		if primes[i] == True:
			primeNums.append(i)

	return primeNums	
run()
