import sys
a = int (sys.argv[1])
b = int (sys.argv[2])
c = int (sys.argv[3])
delta = b**2-4*a*c
if delta < 0:
    print("There is no real solution.")
elif delta == 0:
    print("There are two repeated real number solutions.")
    x = (-b)/(2*a)
    print("Solution(s):", round(x,2))
else:
    x = (-b+ pow(delta, 1/2))/(2*a)
    x2= (-b- pow(delta, 1/2))/(2*a)
    print("There are two solutions")
    print("Solution(s):", round(x,2), round(x2,2))
