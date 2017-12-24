import math

def solve():
	words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
		"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
                "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

	count = 0
	size = 0;
	for hundred in range(0, 10):
		while (count < 20):
			if (hundred == 0):
				print words[count]
				size += len(words[count])

			
			if(hundred > 0):
				hundredsNum = str(words[hundred] + words[28] + words[count])
				
				if((not (count % 10 == 0)) or (count == 10)):
					hundredsNum = str(words[hundred] + words[28] + "and" + words[count])	
				size += len(hundredsNum)	
				print hundredsNum

			count += 1

		tensCount = count

		while (count < 100):
		
			if(hundred == 0):
				num = str(words[tensCount]+words[count%10])
				print num
				size += len(num)

			if(hundred > 0):
				hundredsNum = str(words[hundred] + words[28] + "and"+words[tensCount]+words[count%10])
				size += len(hundredsNum)
				print hundredsNum

			count += 1
			if(count%10 == 0 and count > 20):
				tensCount += 1

		count = 0	
	thousand = words[1] + words[29]
	print thousand
	size += len(thousand)
	print size

solve()
