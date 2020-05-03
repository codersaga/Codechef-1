
t = int(input())
for _ in range(t):
    n = int(input())
    a = int(input())
    s = a + 2*10**n
    print(s)
    b = int(input())
    c = 10**n - b
    print(c)
    d = int(input())
    e = s - (a+b+c+d)
    print(e)
    check = int(input())
    if check < 0:
        exit(0)
    
