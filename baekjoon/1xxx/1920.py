def sort(_seq):
    if(len(_seq) <= 1):
        return _seq
    
    m = len(_seq)//2
    l = _seq[:m]; r = _seq[m:]

    _l = sort(l); _r = sort(r)
    return conquer(_l, _r)

def conquer(_l, _r):
    l = r = 0; _seq = []
    while(l < len(_l) and r < len(_r)):
        if(_l[l] < _r[r]): _seq.append(_l[l]); l += 1
        else: _seq.append(_r[r]); r += 1
    while(l < len(_l)): _seq.append(_l[l]); l += 1
    while(r < len(_r)): _seq.append(_r[r]); r += 1
    return _seq

def inSeq(_seq, _target):
    s_idx = 0; e_idx = len(_seq) - 1

    while(s_idx <= e_idx):
        m_idx = (s_idx + e_idx)//2

        if(_target == _seq[m_idx]): return 1
        elif(_target > _seq[m_idx]): s_idx = m_idx + 1
        else: e_idx = m_idx - 1
    return 0

n = int(input()); seq_a = list(map(int, input().split())) # IN : n, seq_a
m = int(input()); seq_b = list(map(int, input().split())) # IN : m, seq_b

seq_a = sort(seq_a) #sort seq_a

for i in range(m):
    print(inSeq(seq_a, seq_b[i])) #OUT : find a intersection of seq_a with seq_b