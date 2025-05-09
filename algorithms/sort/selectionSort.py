def selectionSort(_seq):
    for i in range(len(_seq) - 1):
        min_idx = i
        for j in range(i + 1, len(_seq)):
            if(_seq[j] < _seq[min_idx]): min_idx = j
        _seq[i], _seq[min_idx] = _seq[min_idx], _seq[i]