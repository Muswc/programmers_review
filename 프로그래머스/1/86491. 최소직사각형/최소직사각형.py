def solution(sizes):
    width = []
    height = []
    
    #리스트[60, 50]...를 돌며 둘 중 큰 값은 width, 작은 값은 height에 저장
    for i in sizes:
        width.append(max(i))
        height.append(min(i))
    
    return max(width) * max(height) #제일 긴 가로 * 제일 긴 세로 길이