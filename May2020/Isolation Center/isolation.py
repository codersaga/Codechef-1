for _ in range(int(input())):
    n, q = map(int, input().split())
    
    s = list(input())
    count = {}
    for letter in s:
        if letter not in count:
            count[letter]=1
        else:
            count[letter]+=1
    
    for _ in range(q):
        pending_len = 0
        c = int(input())
        for key, val in count.items():
            if val-c>0:
                pending_len+=val-c
        print(pending_len)
