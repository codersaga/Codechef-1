t = int(input())
for i in range(t):
    strength, w1, w2, w3 = map(int, input().split())
    if w1+w2+w3 <= strength:
        print(1)
    else:
        move = 0
        if w1 + w2 <= strength:
            print(2)
        elif w2 + w3 <= strength:
            print(2)
        else:
            print(3)
