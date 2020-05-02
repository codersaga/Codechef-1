for _ in range(int(input())):
    n_person = int(input())
    array = list(map(int, input().split()))
    case = dict()
    case[n_person-1]=1  
    for i in range(n_person-1):
        for j in range(i, n_person-1):
            if i not in case:
                case[i]=1
            if array[j+1]-array[j]<=2:
                case[i]+=1
            else:
                i=j
                break

    if array[n_person-1]-array[n_person-2]<=2:
        del case[n_person-1]
        
    cases = []
    i=0
    while i < len(case):
        cases.append(case[i])
        i+=case[i]
    print(min(cases), max(cases))
