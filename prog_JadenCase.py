def solution(s):
    answer = ''
    word_length = len(s)
    # 첫번째 문자가 소문자면 -> 대문자 변경
    # 그 외 -> 유지
    if s[0].islower():
        answer += s[0].upper()
    else:
        answer += s[0]
    
    for i in range(1,word_length):
        if s[i-1] != ' ':               # 이전 문자가 공백이 아니라면
            if s[i].isupper():          # 현재 문자가 대문자면 -> 소문자 변경
                answer += s[i].lower()
            else:
                answer += s[i]
        else:                           # 이전 문자가 공백이면
            if s[i].islower():          # 소문자면 -> 대문자 변경
                answer += s[i].upper()
            else:
                answer += s[i]
    return answer