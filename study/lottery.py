import random

getRand = int(input())
random.seed((getRand*42 + 316) // 43)

nums = [i for i in range(1, 46)]

for _ in range(5):
    seq = random.sample(nums, 6)
    seq.sort()
    print(seq)