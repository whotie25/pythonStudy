tc = int(input()) # IN : test case

for _ in range(tc):
    k = int(input()); n = int(input()) # IN : k, n
    for i in range(n - 1):
        res *= k + n - i
    for i in range(1, n):
        res //= i

    print(res) # OUT : result

# find the number of residents in unit 'n' on the 'k'th floor (n >= 1, k >= 0).
# answer : (k+n)C(n-1)