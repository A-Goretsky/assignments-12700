result = []

def fizzbuzz(start, end):
    for i in range(start, end + 1):
        s = ''
        if i%3 == 0:
            s += "fizz"
        if i%5 == 0:
            s += "buzz"
        if (i%3 != 0 and i%5 != 0):
            s += str(i)
        result.append(s)
 
    for x in result:
        print(x)
    
fizzbuzz(1, 100)
