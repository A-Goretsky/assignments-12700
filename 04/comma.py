spam = ['apples', 'bananas', 'tofu', 'cats']
test2 = ['one']
test3 = ['apples', 'bananas', 'tofu', 'cats', 'apples', 'bananas', 'tofu', 'cats']

def comma(l1):
    res = ''
    lenl1 = len(l1)
    ctr = 1
    for i in l1:
        if (lenl1 == ctr and ctr != 1):
            res += ('and ' + i)
        elif (lenl1 == ctr and ctr == 1):
            res += i
        else:
            res += (i + ', ')
            ctr += 1
    print(res)
    
comma(spam)
comma(test2)
comma(test3)
