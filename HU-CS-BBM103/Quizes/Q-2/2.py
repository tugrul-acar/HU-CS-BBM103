import sys
sumeven = 0
sumtotal = 0
s = sys.argv[1].split(",")
evenlist = []
for i in s:
    if int(i)>0:
        sumtotal += int(i)
        if int(i) % 2 == 0:
            evenlist.append((i))
            sumeven = sumeven + int(i)

print("Even Numbers: ", end='')
print('"'+(','.join(evenlist))+'"')
print("Sum of Even Numbers:",sumeven)
sumrate = (sumeven/sumtotal)
print("Even Number Rate:",round(sumrate,3))
