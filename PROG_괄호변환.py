def check(arr):

    if arr == []:   # 빈 리스트면 => return
        return []
    u,v = [],[]
    l,r = 0,0       # 좌/우 괄호 개수 확인용
    # u 만들기 => l,r 개수 같은 때까지
    for i in range(len(arr)):
        if arr[i] =='(':
            l += 1
        else:
            r += 1
        u.append(arr[i])
        if l == r:
            rem = i+1
            break
    # v 만들기 => 남은 값 다 넣기
    for i in range(rem,len(arr)):
        v.append(arr[i])
    # 올바른 괄호인지 체크 => stack으로 짝맞으면 빼내기
    stack = []
    for i in range(len(u)):
        if not stack:
            stack.append(u[i])
        else:
            if u[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                stack.append(u[i])
    if not stack:       # 올바른 괄호면
        given = check(v)
        return (u + given)
    else:               # 아니면
        now = ['(']
        now += check(v)
        now += [')']
        u.pop()
        u.pop(0)
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        return (now + u)
    
def solution(p):
    answer = ''
    cur = 0 
    ans = check(p)
    answer = ''.join(ans)
    return answer