def freq(n, l):
    ctr = 0
    for i in l:
        if i == n:
            ctr += 1
    return ctr

def min(l):
    num = l[0]
    for i in l:
        if i < num:
            num = i
    return num

def max(l):
    num = l[0]
    for i in l:
        if i > num:
            num = 1
    return num

def mode(l):
    num_List = []
    freq_list = []
    res_List = []
    for i in l:
        if i in num_List:
            pass
        else:
            freq_list.append(freq(i, l))
            num_List.append(i)
    mode_num = max(freq_list) #mode_num = amount of mode
    mode_freq = freq(mode_num, freq_list)
    #####################
    if mode_freq != 1:
        for i in range(mode_freq):
            res_List.append(num_List[freq_list.index(mode_num)])
            num_List = num_List[freq_list.index(mode_num) + 1:]
            freq_list = freq_list[freq_list.index(mode_num) + 1:]
        return res_List
    else:
        return num_List[freq_list.index(mode_num)]
    #mode_num = max(freq_list)
    #if freq(mode_num, freq_list) == 1:
    #    return l[l.index(mode_num)]
    #else:
    #    for i in range(mode_num):
    #        res_List.append(l[l.index(mode_num)])
    #        l = l[l.index(mode_num):]
    #return res_List


print(freq(3, [3, 2, 2, 1, 3, 4, 5, 4, 3, 4, 3]))
print(min([3, 2, 2, 1, 3, 4, 5, 4, 3, 4, 3]))
print(mode([3, 2, 2, 1, 3, 4, 5, 4, 3, 4, 3, 4]))
print(mode([5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 1]))
