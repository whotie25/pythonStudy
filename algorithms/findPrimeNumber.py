def isPrime(_num): #소수 판별 함수
    if (type(_num) != int): return None
    if(_num < 1): return None
    
    if(_num == 1): return False
    if(_num == 2 or _num == 3): return True
        
    for i in range(2, int(_num**0.5) + 1):
        if(_num%i == 0): return False
    
    return True