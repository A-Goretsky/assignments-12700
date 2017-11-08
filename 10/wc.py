import collections

###HOMEWORK CODE BEGINS
def rem_non_alpha(w):
    return "".join([l for l in w if l.isalpha()])

def sort_words(word_list):
    d = collections.defaultdict(lambda: [])
    for w1, w2 in zip(word_list, word_list[1:]):
        d[w1].append(w2)
    return d

def next_word_main(f):
    with open(f) as file:
        text = file.read()
        list_of_words = [rem_non_alpha(w.lower()) for w in text.split()]
        return sort_words(list_of_words)

d = next_word_main('hamlet.txt')
print(d)
###HOMEWORK CODE ENDS

###OLD CODE BEGINS
def rp_OLD(w):
    result = ""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd_OLD(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def bwcff_OLD(f):
    f = open(f).read()
    l = []
    for w in f.split():
        w = w.lower()
        w = rp(w)
        l.append(w)
    d = bwcd(l)
    return d

def rem_non_alpha(w):
    return "".join([l for l in w if l.isalpha()])

def count_words(wordlist):
    d = collections.defaultdict(lambda: 0)
    for w in wordlist:
        d[w] += 1
    return d

def word_count_dict(f):
    with open(f) as file:
        text = file.read()
        list_of_words = [rem_non_alpha(w.lower()) for w in text.split()]
        word_count = count_words(list_of_words)
        return word_count

#d = word_count_dict("hamlet.txt")
#v = list(d.values())
#print(d)
#list_comprehension

#Stuff
def placeholder():
    l = [x for x in range(10)]
    l = [5 for x in range(10)]
    l = [l for l in "hello world"]
#Stop words concept

#import dis
#dis.dis(wc.rem_non_alpha)
#(Disassemble the function)
"""
'to': ['be', 'be']
'be': ['or']
'or': ['not']
'not': ['to']
"""
#markov chain
