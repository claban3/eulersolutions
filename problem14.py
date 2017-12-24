from time import time
t = time()
def gen(num, nums, lengths):
  curr = num
  count = 0
  done = False
  while not done and curr != 1:
    if curr == nums:
      count += lengths 
      done = True
      count -= 1
    if curr % 2 != 0:
      curr = (curr * 3) + 1
      curr = curr/2 
      count += 1 
    else:
      curr = curr / 2
    count += 1
  return count

def solve():
  nums = 1
  lengths = 1
  m = 0 
  mSNum = 0
  c = 0 
  for i in xrange(2, 1000000):
    c = gen(i, nums, lengths)
    if c > m:
      m = c
      mSNum = i
      nums = i
      lengths = c
  print mSNum
solve()

ft = time() - t
print ft
