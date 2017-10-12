#UpperCase 65 - 90
#LowerCase 97 - 122
import math as m

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

def rotate_char(c, r):
    v = ord(c)
    v -= 97
    v - (v+r)%26
    v += 97
    result = chr(v)
    print(result)
    return result

def rotate_string(s, r):
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter, r)
        result += letter
    return result

def distance_form(l1, l2):
    #Euclidian distance between l1 and l2. If the lists are of
    #different lengths, go to the length of the shorter one.
    length = len(l1)
    if length < len(l2):
        length = len(l2)
    sum = 0
    for i in range(length):
        sum = sum+((l1[i]-l2[i])**2)
    d = m.sqrt(sum)
    return d

l1 = [1, 2, 3]
l2 = [10, 2, 3]

def build_frequency_vector(s):
    #count the letters in the string
    #count each letter to see how many times it appears.
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    return v


def print_vector_table(v):
    s = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i], " : ", v[i])

def build_vect_list(s):
    for i in range(0, 26):
        freq_vect_list.append(build_frequency_vector(encodeList[i]))

sentence = "this is the long sentence that i am using for the project for homework number six because it is different from the one used in class, but still very long."
freq_vect_list = []
encodeList = []

def decode(s):
    for x in range(26):
        encodeList.append(encode_string(s, x))
    build_vect_list(s)
    index = 0
    for i in range(26):
        if distance_form(freq_vect_list[i], stat) < distance_form(freq_vect_list[index], stat):
            index = i
    return encode_string(s, index)

f = open("anna_karenina.txt")
stat = build_frequency_vector(f.read().lower())
print(decode(sentence))
#print_vector_table(0)
#f = build_frequency_vector("This is a test")
#s = "this is a longer sentence with more letters so hopefully it will be closer to the real distribution"
#f = build_frequency_vector(s)
#print_vector_table(f)
#print("~~~~~~~~~~~~")
#r = encode_string(s, 3)
#r = build_frequency_vector(r)
#print_vector_table(r)
#print_vector_table(f)

#print(encode_letter('a', 3))
##print(encode_letter('y', 3))
#print(encode_string('hello', 3))
##print(encode_string('hello world!', 3))
#print(encode_string('xylophone', 3))
#print(full_encode('hello'))
#print(full_encode('hello world!'))
