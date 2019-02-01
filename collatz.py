# Collatz Sequence

def collatz(number):
    if number == 1:
        return
    if number % 2 == 0:
        result = number // 2
        print(result)
        collatz(result)
    else:
        result = 3 * number + 1
        print(result)
        collatz(result)

input = int(input())
collatz(input)