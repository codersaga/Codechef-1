c, b = map(float, input().split())
if c%5==0 and b-c-0.5 >=0:
    print(b-c-0.50)
else:
    print(b)
