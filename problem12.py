import math
from time import time
t = time()
def divisors(num):
  numDiv = 0
  for i in xrange(1, int(math.ceil(math.sqrt(num)))-1):
    if num % i == 0:
      if i ** 2 == num:
	numDiv += 1
      else:
	numDiv += 2
  return numDiv
def run():
  triNum = 1
  for i in xrange(2, 10000000):
    triNum += i
    if divisors(triNum) > 500:
      print triNum
      break

run()
ft = time() - t
print ft


