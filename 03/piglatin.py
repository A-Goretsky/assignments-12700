def piglatinify(s):
    if (s[0] in 'aeiou'):
        return s + "ay"
    else:
        return s[1:] + s[0] + "ay"
    
print(piglatinify("latin"))
print(piglatinify("orange"))