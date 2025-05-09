def mergeSort(_seq):
    if (len(_seq) <= 1):
        return _seq
    
    mid = len(_seq)//2 #division
    l = _seq[:mid]
    r = _seq[mid:]

    _l = mergeSort(l)
    _r = mergeSort(r)
    return conquer(_l, _r)

def conquer(_l, _r):
    l = r = 0
    res = []

    while (l < len(_l) and r < len(_r)):
        if(_l[l] < _r[r]): res.append(_l[l]); l += 1
        else: res.append(_r[r]); r += 1
    while l < len(_l): res.append(_l[l]); l += 1
    while r < len(_r): res.append(_r[r]); r += 1
    return res