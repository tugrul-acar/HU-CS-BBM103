import sys
def chainbomb(b, a, st):
    sum2 = 0
    if st == 1:
        silinencolon = matris[b]
        del matris[b]
        sum2 += bombscore([],silinencolon)
        if "X" in silinencolon:
            error = 0
            while error == 0:
                try:
                    indeks = silinencolon.index("X")
                    sum2 += chainbomb(b, indeks, 2)
                    del silinencolon[indeks]
                except:
                    error = 1
        return sum2

    if st ==  2:
        silinensatır = []
        for i in range(len(matris)):
            try:
                silinensatır.append(matris[i][a])
            except IndexError:
                None
        sum2 += bombscore(silinensatır,[])
        for i in range(len(matris)):
            del matris[i][a]
        if "X" in silinensatır:
            error = 0
            while error == 0:
                try:
                    indeks = silinensatır.index("X")
                    sum2 += chainbomb(indeks,a,1)
                    del silinensatır[indeks]
                except:
                    error = 1
        return sum2

def calculate(sayi, harf):
    if harf == "B":
        return (sayi+1)*9
    if harf == "G":
        return (sayi+1) * 8
    if harf == "W":
        return (sayi+1) * 7
    if harf == "Y":
        return (sayi+1) * 6
    if harf == "R":
        return (sayi+1) * 5
    if harf == "P":
        return (sayi+1) * 4
    if harf == "O":
        return (sayi+1) * 3
    if harf == "D":
        return (sayi+1) * 2
    if harf == "F":
        return (sayi+1) * 1
def finder(b, a, letter):
    if matris[b][a] != "X" and " ":
        over = False
        try:
            if matris[b + 1][a] == letter:
                p.append(" ")
                matris[b][a] = " "
                matris[b + 1][a] = " "
                over = True
                finder(b+1,a,letter)
        except IndexError:
            None
        try:
            if matris[b - 1][a]== letter and b-1 >= 0:
                p.append(" ")
                matris[b][a] = " "
                matris[b - 1][a] = " "
                over = True
                finder(b-1,a,letter)
        except IndexError:
            None
        try:
            if matris[b][a + 1]== letter:
                p.append(" ")
                matris[b][a] = " "
                matris[b][a + 1] = " "
                over = True
                finder(b,a+ 1,letter)
        except IndexError:
            None
        try:
            if matris[b][a - 1]== letter and a-1 >= 0:
                p.append(" ")
                matris[b][a] = " "
                matris[b][a - 1]= " "
                over = True
                finder(b,a - 1,letter)
        except IndexError:
            None
        if over == True:
            return over, calculate(len(p), letter)
        else:
            return over,0

    elif matris[b][a] == "X":
        silinensatır = []
        silinencolon = matris[b]
        for i in range(len(matris)):
            try:
                silinensatır.append(matris[i][a])

            except IndexError:
                None
        del silinensatır[b]
        sum1 = bombscore(silinensatır, silinencolon)
        for i in range(len(matris)):
            del matris[i][a]
        del matris[b]
        if "X" in silinensatır:
            error = 0
            while error == 0:
                try:
                    indeks = silinensatır.index("X")
                    sum1 += chainbomb(indeks,a,1)
                    del silinensatır[indeks]
                except:
                    error = 1
        if "X" in silinencolon:
            error = 0
            while error == 0:
                try:
                    indeks = silinencolon.index("X")
                    sum1 += chainbomb(b, indeks, 2)
                    del silinencolon[indeks]
                except:
                    error = 1
        return b, sum1

def bombscore(satır = [],colon= []):
    score1 = 0
    for i in satır:
        if i == "B":
            score1 += 9
        if i == "G":
            score1 += 8
        if i == "W":
            score1 += 7
        if i == "Y":
            score1 += 6
        if i== "R":
            score1 += 5
        if i == "P":
            score1 += 4
        if i == "O":
            score1 += 3
        if i == "D":
            score1 += 2
        if i == "F":
            score1 += 1
    for i in colon:
        if i == "B":
            score1 += 9
        if i == "G":
            score1 += 8
        if i == "W":
            score1 += 7
        if i == "Y":
            score1 += 6
        if i == "R":
            score1 += 5
        if i == "P":
            score1 += 4
        if i == "O":
            score1 += 3
        if i == "D":
            score1 += 2
        if i == "F":
            score1 += 1
    return score1

def gameover(game):
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            try:
                if matris[i][j + 1] == matris[i][j] and matris[i][j] != " ":
                    return True
            except IndexError:
                None
            try:
                if matris[i+1][j] == matris[i][j] and matris[i][j] != " ":
                    return True
            except IndexError:
                None
            try:
                if matris[i][j] == "X" and matris[i][j] != " ":
                    return True
            except IndexError:
                None
def shorter(a):
    for i in range(len(column)):
        for j in range(len(matris)):
            if a[j][i] == " ":
                None
            else:
                o = True
def checker(a,b):
    try:
        if matris[a][b] == " ":
            return 0
        else:
            return 1
    except IndexError:
        return 0

def maker():
    cut = 0
    for i in range(len(matris[0]) - 1, -1, -1):
        for j in range(matrislength):
            if matris[j][i] == " ":
                cut += 1
            else:
                cut = 0
            if cut == matrislength:
                for t in range(matrislength):
                    del matris[t][i]
                cut = 0
    cut = 0
    for i in range(matrislength):
        for j in range(len(matris[0])):
            try:
                if matris[i][j] == " ":
                    cut += 1
                else:
                    cut = 0
            except:
                None
            if cut == len(matris[0]):
                try:
                    del matris[i]
                except:
                    None

with open(f"{sys.argv[1]}") as text:
    matris = [[], []]
    y = 0
    c1 = [" "]
    for i in text:
        if "\n" in i:
            i = i[:-1]
        i = i.split(" ")
        matrislength = len(i)
        if len(matris) != matrislength:
            for a in range(matrislength-2):
                matris.append([])
        for j in range(matrislength):
            matris[j].append(i[j])
score = 0
column = len(matris[0])
for i in range(matrislength):
    matris[i] = matris[i][::-1]
for i in range(len(matris[0]) - 1, -1, -1):
    for j in range(matrislength):
        if j == matrislength - 1:
            print(matris[j][i])
        else:
            print(matris[j][i], end=" ")
print(f"\nYour score is {score}")

loop = gameover(matris)
while loop:
    loop = False
    column = len(matris[0])
    matrislength = len(matris)
    x, y = input("\nPlease enter a row and column number: ").split(" ")
    x1 = int(y)
    y1 = column - int(x) - 1
    tru = checker(x1,y1)
    while tru == 0:
        print("\nPlease enter a valid size!")
        x, y = input("\nPlease enter a row and column number: ").split(" ")
        x1 = int(y)
        y1 = column - int(x) - 1
        tru = checker(x1, y1)
    chosen = matris[x1][y1]

    p = []
    j,sumnumber = finder(x1,y1,chosen)
    for i in range(len(matris)):
        for j in range(len(matris[0]) - 1, -1, -1):
            if matris[i][j] == " ":
                del matris[i][j]
                matris[i].append(" ")
    score += int(sumnumber)
    column = len(matris[0])
    matrislength = len(matris)
    maker()
    print("    ")
    column = len(matris[0])
    matrislength = len(matris)
    for i in range(len(matris[0]) - 1, -1, -1):
        for j in range(matrislength):
            if j == matrislength-1:
                print(matris[j][i])
            else:
                print(matris[j][i], end=" ")
    print(f"\nYour score is {score}")
    loop = gameover(matris)
print("     ")
print("Game over!")
