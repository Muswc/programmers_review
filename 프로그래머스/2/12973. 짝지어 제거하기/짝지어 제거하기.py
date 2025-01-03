def solution(s):
    answer = -1
    check = []
    
    for i in s:
        if not check:
            check.append(i)
        elif check[-1] == i:
            check.pop()
        else:
            check.append(i)
    

    return 0 if check else 1