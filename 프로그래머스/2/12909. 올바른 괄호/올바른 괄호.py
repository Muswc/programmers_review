def solution(s):
    answer = True
    check = []
    
    for i in s:
        if i == '(':
            check.append('(')
        elif i == ')':
            if len(check) == 0:
                return False
            else:
                check.pop()
                
    if len(check) != 0:
        return False

    return True