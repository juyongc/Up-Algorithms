def to_check(s):
    stack = []
    pairs = {'(':')','[':']','{':'}'}
    # 모든 문자열 확인
    # '({[' => 스택에 추가 
    # ']})' => 이전 스택값이 짝이 맞으면 같이 삭제 or return False
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] in pairs and ch == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    # 스택에 남은 값이 없어야 올바른 문자열
    if not stack:
        return True
    else:
        return False

def solution(s):
    answer = 0
    # 왼쪽으로 한칸씩 이동하면서 확인하기
    for i in range(len(s)):
        check = to_check(s[i:] + s[:i])
        if check:
            answer += 1
    return answer