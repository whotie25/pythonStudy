def search(_seq, _target):
    s_idx = 0; e_idx = len(_seq) - 1

    while(s_idx <= e_idx):
        m_idx = (s_idx + e_idx)//2

        if(_target == _seq[m_idx]):
            return m_idx
        elif(_target < _seq[m_idx]):
            e_idx = m_idx - 1
        else:
            s_idx = m_idx + 1
    return -1
