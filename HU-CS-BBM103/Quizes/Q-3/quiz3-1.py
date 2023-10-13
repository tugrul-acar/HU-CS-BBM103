import sys

x = int (sys.argv[1])
n = int (sys.argv[2])
number = x**n
array = [""]*100

array[0] = str(x)+"^"+str(n)
array[1] = str(number)
c = 2

sum = number
a = str(number)
l = len(a)
y =0


if number < 10:
    u = 1
else:
    y=int(1)

while y == 1:

    sum = 0
    for i in range(l):
        array[c] = array[c]+" + "+str(a[i])
        sum += int(a[i])
    array[c] = array[c][3:]
    c = c+1
    array[c] = str(sum)
    c = c+1


    if sum > 9:
        y = 1
        a = str(sum)
        l = len(str(sum))
    else:

        y = 0


for i in range(c):
    if i==c-1:
        print(array[i])
    else:
        print(array[i],end= " = ")