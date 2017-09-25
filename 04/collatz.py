def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
    
def userCollatz():
    inputNum = int(input("Integer? "))
    res = 0
    while res != 1:
        res = collatz(inputNum)
        inputNum = res
        
userCollatz()