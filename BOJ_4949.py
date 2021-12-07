import sys
inputs = sys.stdin.readline

while True:
    words = inputs().rstrip()
    if words == '.':
        break

    stack = []

    for word in words:
        if word == "(" or word =="[":   # 왼괄호 => 추가
            stack.append(word)

        elif word == ")" or word == "]":    # 우괄호 => 상황 분석
            if not stack:                   # 스택에 없으면 => 아웃
                stack.append(word)
                break
            else:                           # 스택에 값이 있으면
                if word == ")" and stack[-1] == "(":    # 가능한 경우
                    stack.pop()
                elif word == "]" and stack[-1] == "[":  # 가능한 경우
                    stack.pop()
                else:                                   # 불가 => 아웃
                    stack.append(word)
                    break
    # 상황별 출력
    if stack:
        print("no")
    else:
        print("yes")