def solution(s):
    arr = s.split(' ')
    
    for i in range(len(arr)):
        #capitalize()는 문장의 첫 글자, title()는 모든 단어의 첫 글자를 대문자로 만듬
        arr[i] = arr[i].capitalize()
        
    return ' '.join(arr)