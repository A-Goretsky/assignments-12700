#UpperCase 65 - 90
#LowerCase 97 - 122

def encode_letter(c, r):
    if ord(c) < 90:
        asc = ord(c) + r
        if asc > 90:
            asc = (asc % 90) + 66
    else:
        asc = ord(c) + r
        if asc > 122:
            asc = (asc % 122) + 96
    res = chr(asc)
    return res

def encode_string(s, r):
    ans = ''
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            ans += encode_letter(i, r)
        else:
            ans += i
    return ans

def full_encode(s):
    ans = ''
    for i in range(1, 26):
        ans += encode_string(s, i) + '\n'
    ans = ans.strip('\n')
    return ans

print(encode_letter('a', 3))
print(encode_letter('y', 3))
print(encode_string('hello', 3))
print(encode_string('hello world!', 3))
print(encode_string('xylophone', 3))
print(full_encode('hello'))
print(full_encode('hello world!'))
