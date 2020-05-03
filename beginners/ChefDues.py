for _ in range(int(input())):
    month = int(input())
    arr = list(map(int, input().split()))
    due = c = 0
    for i in range(len(arr)):
        if arr[i]==0:
            break
        else:
            c+=1
    for i in range(c,len(arr)):
        if arr[i]==1:
            due+=100
        else:
            due+=1100
    print(due)
    
    
