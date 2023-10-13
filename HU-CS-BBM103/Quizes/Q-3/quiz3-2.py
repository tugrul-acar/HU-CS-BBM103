import sys

numbers = sys.argv[1].split(",")
number1 = []
def find_numbers(numbers):
    if int(numbers[0]) == 1:
        n = 1

        step = int(2)

        del numbers[step - 1::step]


        n = 1

    else:
        n = 0

    step = int(number1[n])
    while int(step) < len(number1):
        del numbers[step - 1::step]

        if str(step) in str(number1):
            n += 1
            step = int(number1[n])
        else:
            step = int(number1[n])
    print(*numbers, sep=" ")


j = int(0)
for i in range(len(numbers)):
    if int(numbers[j]) <= 0:
        a = str(numbers[j])
        numbers.remove(a)
    else:
        j += 1
for i in numbers:
    number1.append(int(i))
number1.sort()


find_numbers(number1)