def solution(brack):
    answer = True
    check = []
    for b in brack:
        if b == '(':    # 왼 괄호 => append
            check.append(b)
        else:           # 우 괄호
            if check:   # 리스트에 뭔가 있으면
                if check[-1] == '(':    # 왼괄호면 => pop
                    check.pop()
                else:                   # 우괄호면 => break
                    break
            else:       # 없으면 => 넣고, break
                check.append(b)
                break
    if check:           # 리스트에 뭔가 있으면 => false
        answer = False
    return answer