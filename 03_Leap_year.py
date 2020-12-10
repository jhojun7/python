YEAR = int(input())
if YEAR % 400 == 0:
	print("Leap Year")
	
elif YEAR % 100 == 0:
	print("Not Leap Year")
		
elif YEAR % 4 == 0:
	print("Leap Year")
	
else:
	print("Not Leap Year")