def solution(s):
    answer = 1

    stack = []
    i = 0
    # 이전 스택값이랑 비교해서
    # 같으면 pop / 다르면 append
    while i < len(s):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        i += 1
    
    if stack:
        answer = 0
    return answer