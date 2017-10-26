def divide(A, B, u):
    res = 0
    res = (int)(u // (A / B))
    #print(5/10)
    #print(1/2)
    #print(1 / (1/2))
    #print(1 / (5/10))
    print(res)

divide(3, 4, 4.5)
divide(5, 10, 1)
divide(1, 2, 1)
divide(3, 4, .5)
#3/4, 1 1/2, 2 1/4, 3, 3 3/4

def encode(s):
    if len(s) == 0:
        print("String is Empty")
        return
    res = []
    temp = s[0]
    ctr = 0
    act = 0
    for i in s:
        if i == temp:
            ctr += 1
        else:
            res.append(ctr)
            res.append(temp)
            ctr = 1
            temp = i
            act = 1
    res.append(ctr)
    res.append(temp)
    print(res)

encode("aaaabbb")
encode("aaaa")
encode("aaaabbbcccc")
encode("aabcccdeeeeaaa")
encode("")

def score(w):
    sum = 0
    letter = 0
    for i in w:
        if i in 'AEIOULNRST':
            letter = 1
        elif i in 'DG':
            letter = 2
        elif i in "BCMP":
            letter = 3
        elif i in "FHVWY":
            letter = 4
        elif i in "K":
            letter = 5
        elif i in "JX":
            letter = 8
        elif i in "QZ":
            letter = 10
        sum += letter
    print(sum)
    return sum

def score2(w):
    res = 0
    dict = {
    1:['A', 'E', 'I', 'O', 'L', 'N', 'R', 'S', 'T'],
    2:['D', 'G'],
    3:['B', 'C', 'M', 'P'],
    4:['F', 'H', 'V', 'W', 'Y'],
    5:['K'],
    8:['J', 'X'],
    10:['Q','Z']}
    for key, value in dict.items():
        w = w.upper()
        for i in w:
            if i in value:
                res += key
    print(res)
    return res

score2('A')
score2("hello")
score2("zqj")
    #1'AEIOULNRST'
    #2'DG'
    #3'BCMP'
    #4'FHVWY'
    #5'K'
    #8'JX'
    #10'QZ'
    #res = dict[w]
    #print(res)

#score('A')
#score("HELLO")
