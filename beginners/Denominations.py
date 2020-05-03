for _ in range(int(input())):
    den = int(input())
    notes = 0
    while den!=0:
        if den >= 100:
            den-=100
            notes+=1
        elif den >= 50:
            den-=50
            notes+=1
        elif den >= 10:
            den-=10
            notes+=1
        elif den >= 5:
            den-=5
            notes+=1
        elif den >= 2:
            den-=2
            notes+=1
        elif den >= 1:
            den-=1
            notes+=1
    print(notes)
