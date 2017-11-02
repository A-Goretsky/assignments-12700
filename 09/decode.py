def encode(s):
    if len(s) == 0:
        print("String is Empty")
        return
    res = []
    temp = s[0]
    ctr = 0
    for i in s:
        if i == temp:
            ctr += 1
        else:
            res.append(ctr)
            res.append(temp)
            ctr = 1
            temp = i
    res.append(ctr)
    res.append(temp)
    print(res)

encode("aaaabbb")
encode("aaaa")
encode("aaaabbbcccc")
encode("aabcccdeeeeaaa")
encode("")

def rle_decode(lis):
    res = ''
    ctr = 0
    while ctr < len(lis):
        if isinstance(lis[ctr], int):
            res += (lis[ctr] * lis[ctr+1])
            ctr += 2
        else:
            res += lis[ctr]
            ctr += 1
    print(res)
    return res

rle_decode([2,'a', 3, 'b', 'c', 2,'d'])
rle_decode([4,'a', 'x', 5, 'z'])
