t = int(input())
for _ in range(t):
    p,q = map(int, input().split())
    print(max([p,q]), p+q)
