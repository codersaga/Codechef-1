for _ in range(int(input())):
    x, y, l, r = map(int, input().split())

    '''
    max_val = 0
    p = 0
    for i in range(l, r):
        if (x & i) * (y & i) > max_val:
            p = i
            max_val = (x & i) * (y & i)
    '''
    z = x | y if (x != 0 and y != 0) else 0
    if z <= r:
        print(z)
     
    else:
        n = 0
        mult = 1
        while n <= r or (x != 0 and y != 0):
            n += (x & 1 | y & 1)*mult
            x = x//2
            y = y//2
            mult *= 2
        print(n)
