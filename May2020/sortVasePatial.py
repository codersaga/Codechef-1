for _ in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))
    robot_swaps = []
    for i in range(m):
        x,y = map(int, input().split())
        robot_swaps.append((x,y))
        robot_swaps.append((y,x))
    minute = 0
    minute_rev = 0
    mod_arr=array
    if m==0:
        for i in range(n):
            mod_arr = mod_arr[:n-i]
            max_el_ind = mod_arr.index(max(mod_arr))
            if (mod_arr[max_el_ind]!=mod_arr[-1]):
                mod_arr[max_el_ind], mod_arr[-1] = mod_arr[-1], mod_arr[max_el_ind]
                minute+=1
        print(minute)
    else:
        for i in range(n):
            mod_arr = mod_arr[:n-i]
            max_el_ind = mod_arr.index(max(mod_arr))
            if (mod_arr[max_el_ind]!=mod_arr[-1]):
                mod_arr[max_el_ind], mod_arr[-1] = mod_arr[-1], mod_arr[max_el_ind]
                if (mod_arr[max_el_ind], mod_arr[-1]) not in robot_swaps:
                    minute+=1
        mod_arr = array
        for i in range(n):
            min_el_ind = mod_arr.index(min(mod_arr[i:n]))
            if (mod_arr[min_el_ind]!=mod_arr[i]):
                mod_arr[min_el_ind], mod_arr[i] = mod_arr[i], mod_arr[min_el_ind]
                if (mod_arr[min_el_ind], mod_arr[i]) not in robot_swaps:
                    minute_rev+=1
        print(min([minute, minute_rev]))
