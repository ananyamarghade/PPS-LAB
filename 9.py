year = int(input ("Enter a year: "))
if (year%400==00) or (year%4==0 or year%100==0):
	print(year,"is a leap year")
else:
	print(year,"is not a leap year")