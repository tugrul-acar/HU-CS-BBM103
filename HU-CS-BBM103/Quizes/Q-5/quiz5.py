import sys
gameover = 0
operands = []
compare = []
result = []
try:
    try:
        with open(f"{sys.argv[1]}")as text1:
            for i in text1:
                if "\n" in i:
                    i = i[:-1]
                line = i.split(" ")
                operands.append(line)
    except IndexError:
        print("IndexError: number of input files less than expected.")
        gameover = 1
    except IOError:
        print(f"IOError: cannot open {sys.argv[1]}")
        gameover = 1

    try:
        with open(f"{sys.argv[2]}")as text2:
            for i in text2:
                if "\n" in i:
                    i = i[:-1]
                line = i.split(" ")
                compare.append(line)
    except IndexError:
        print("IndexError: number of input files less than expected.")
        gameover = 1
    except IOError:
        print(f"IOError: cannot open {sys.argv[2]}")
        gameover = 1

    if gameover == 0:
        for i in range(len(operands)):
            print("------------")
            result = []

            try:
                result = []
                numbers = operands[i]
                number1 = float(numbers[0])
                number2 = float(numbers[1])
                number1 = int(number1)
                number2 = int(number2)
                number3 = float(numbers[2])
                number4 = float(numbers[3])
                for number in range(int(number3), int(number4+1)):
                    
                    if number % number1 == 0 and number % number2 != 0:
                        result.append(str(number))
                print("My results:             ",*result,sep=" ")
                print("Results to compare:     ",*compare[i],sep=" ")
                assert result == compare[i]
                print("Goool!!!")
            except ValueError:
                print("ValueError: only numeric input is accepted.")
                print("Given input:", *operands[i], sep=" ")
            except IndexError:
                print("IndexError: number of operands less than expected.")
                print("Given input:",*operands[i],sep=" ")
            except ZeroDivisionError:
                print("ZeroDivisionError: You can’t divide by 0.")
                print("Given input:", *operands[i], sep=" ")
            except AssertionError:
                print("AssertionError: results don’t match.")
            except:
                print("kaBOOM: run for your life!")
finally:
    print("˜ Game Over ˜")