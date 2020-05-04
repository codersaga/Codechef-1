for _ in range(int(input())):
    
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    
    
    def notSortable(length, array):
        AlreadySortedCount = 0
        for i in range(length):
            if array[i]==i+1:
                AlreadySortedCount+=1
         
        if (length-AlreadySortedCount)%3==0:
            result = False    
        else:
            result = True
        return result, AlreadySortedCount


    def checkMisplace(subArray):
        if min(subArray)==subArray[-1] and max(subArray)!=subArray[0]:
            return sorted(subArray)
        if max(subArray)==subArray[0] and min(subArray)!=subArray[-1]:
            return reversed(subArray)
        return []

    operations = 0
    operators = []
    isSorted = False
    index = 0
    subArray=[]
    elements_checked = 0
    while operations <= k & index < n:
        notSorted, alreadyPlaced = notSortable(n, array)
        if (notSorted):
            print("not Sortable")
            isSorted = False
            break
        if isSorted:
            print("sorted")
            break
        if array[index]!=index+1 and len(subArray)!=3:
            subArray.append(array[index])
            elements_checked += 1
        if len(subArray)==3:
            if checkMisplace(subArray)==[]:
                break
            operators.append(checkMisplace((subArray)))
            operations+=1
            subArray=[]
            if alreadyPlaced+elements_checked==n:
                isSorted = True
        index+=1
            
            
        
    
    if not isSorted:
        print(-1)
    if isSorted and operations<=k:
        print(operations)
        for i in range(operations):
            print(operators[i][0], operators[i][1], operators[i][2])
        
