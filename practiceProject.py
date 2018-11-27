def collatz(number):
    if number  % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)

print('Enter a number')
userNum = input()
myNum = int(userNum)

collatz(myNum)

while myNum != 1:
    collatz(myNum)
    
