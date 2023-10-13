print("<-----RULES----->")
print("1. BRUSH DOWN")
print("2. BRUSH UP")
print("3. VEHICLE ROTATES RIGHT")
print("4. VEHICLE ROTATES LEFT")
print("5. MOVE UP TO X ")
print("6. JUMP")
print("7. REVERSE DIRECTION")
print("8. VIEW THE MATRIX")
print("0. EXIT")
print("Please enter the command with a plus sign (+) between them.")
p = 1

while p == 1:
    codeuser = input("").split("+")
    length = len(codeuser)
    for i in range(1, length):
        if (int(codeuser[i]) < 0) or (int(codeuser[i]) > 8):
            if int(codeuser[i]) < 50:

                print("You entered an incorrect command. Please try again!")
                p = 1
                break
            elif int(codeuser[i]) > 50:
                for j in codeuser[i][1]:
                    if j == "_":
                        p = 0
                    else:
                        print("You entered an incorrect command. Please try again!")
                        p = 1




            else:
                print("You entered an incorrect command. Please try again!")
                p = 1
                break
        else:
            p = 0

length = len(codeuser)
u = 0
b = " "
y = '*'
a = "+"
n = int(codeuser[0])
array = [[[],[]],[[],[]]]


for i in range(n-2):
    array.append([[],[]])


for j in range(n):
    for i in range(n-2):
        array[j].append([])



for j in range(n):
    for i in range(n):
        array[j][i] = " "


brush = int(0)
rotate = int(4)
x1 = 0
y1 = 0


for i in range(1,length):
    kod = codeuser[i]
    if kod == "1":
        brush = 1
        array[y1][x1] = y
    if kod == "2":
        brush = 0
    if kod == "3":
        rotate +=1
    if kod == "4":
        rotate -=1
    if int(kod) > 50:
        distance = int(kod) % 50
        if brush == 0:
            if int(rotate)%4 == 0:
                x1 = x1 + distance - n
                if x1 < 0:
                    x1 += n
            if int(rotate)%4 == 1:
                y1 = y1 + distance - n
                if y1 < 0:
                    y1 += n
            if int(rotate)%4 == 2:
                x1 = x1-distance
                if x1 < 0:
                    x1 += n
            if int(rotate)%4 == 3:
                y1 = y1-distance
                if y1 < 0:
                    y1 += n
        if brush == 1:

            if int(rotate)%4 == 0:
                for i in range(distance+1):
                    array[y1][x1+i-n]=y
                x1 = x1 + distance - n
                if x1 < 0:
                    x1 = x1 + n
            if int(rotate)%4 == 1:
                for i in range(distance+1):
                    array[y1+ i-n][x1] = y
                y1 = y1 + distance - n
                if y1 < 0:
                    y1 += n

            if int(rotate)%4 == 2:
                for i in range(distance+1):
                    array[y1][x1-i] = y
                x1 = x1-distance
                if x1 < 0:
                    x1 = x1 + n
            if int(rotate)%4 == 3:
                for i in range(distance+1):
                    array[y1-i][x1] = y
                y1 = y1-distance
                if y1 < 0:
                    y1 += n
    if kod == "6":
        distance = 3
        brush = 0
        if brush == 0:
            if int(rotate)%4 == 0:
                x1 = x1 + distance - n
                if x1 < 0:
                    x1 += n
            if int(rotate)%4 == 1:
                y1 = y1 + distance - n
                if y1 < 0:
                    y1 += n
            if int(rotate)%4 == 2:
                x1 = x1-distance
                if x1 < 0:
                    x1 += n
            if int(rotate)%4 == 3:
                y1 = y1-distance
                if y1 < 0:
                    y1 += n


    if kod == "7":
        rotate += 2
    if kod == "8":
        print("+" * (n + 2))
        for i in range(0, n):
            print("+", *array[i], sep='', end="+\n")
        print("+" * (n + 2))
    if kod == "0":
        break







