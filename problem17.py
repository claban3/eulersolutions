def solve():
	words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
		"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
                "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
		
	
	count = 1
	size = 0
	while(count<1000):
		if(count <= 20):
			size += len(words[count])
		if(count <= 100):
			size += len(words[(count - 20)//10 + 20]) + len(words[count%10])
		else:
			size += len(words[count//100]) + len(words[((count-((count//100)*100)) - 20)//10 + 20 ]) + len(words[count%10]) + 3
	print size + 11

solve()
