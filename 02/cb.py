def string_times(str, n):
    ans = str * n
    return ans

def front_times(str, n):
    ans = str[:3] * n
    return ans

def string_bits(str):
    return str[::2]

def lone_sum(a, b, c):
    if (a==b and b==c):
        return 0
    elif (a==b):
        return c
    elif (b==c):
        return a
    elif (a==c):
        return b
    else:
        return a + b + c
    
#Lone Sum Alternate
def lone_sum2(a, b, c):
    sum = 0
    if a != b and b != c: sum += b
    if c != a and c != b: sum += c
    if a != b and a != c: sum += a
    return sum

def string_splosion(str):
    ctr = 1
    ans = ""
    for i in range(len(str) + 1):
        ans += str[:i]
    return ans
        
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)
    
def caught_speeding(speed, is_birthday):
    if (speed >= 81):
        if (is_birthday == False or speed > 85):
            return 2
        else: return 1
    elif (speed >= 61):
        if (is_birthday == False or speed > 65):
            return 1
        else: return 0
    else: return 0
    

print(caught_speeding(86, True))
print(caught_speeding(66, False))
print(caught_speeding(65, True))
print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
print(string_splosion('People')) 
print(string_splosion('ab'))
print(string_splosion('abc'))
print(string_splosion('Code'))    
print(lone_sum2(1, 2, 3))
print(lone_sum2(3, 2, 3))
print(lone_sum2(3, 3, 3))
print(front_times("a", 3))
print(string_bits("hello"))
print(string_bits("hi"))
print(string_bits("Heeololeo"))