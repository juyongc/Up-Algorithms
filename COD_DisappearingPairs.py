def solution(S):
    
    stack = []

    for i in range(len(S)):
        if stack:
            if stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        else:
            stack.append(S[i])
    ans = ''.join(stack)
    
    return ans