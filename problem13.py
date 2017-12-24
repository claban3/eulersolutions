def run():
  file = open("bignum.txt", "r")
  sum = 0
  for char in file:
    sum += int(char)
  ssum = str(sum)
  print ssum[:10]
run()  
