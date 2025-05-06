r=float(input("Enter the radius : "))
area = 3.14*r*r
if r<0 or r>100:
	print("Enter a positive value upto 100")
else:
	print("Area of circle =",format(area, '.6f'))