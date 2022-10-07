import sys
inputs = sys.stdin.readline

ppap = input()
stack = []
flag = 1
## PPAP 없애기
for i in range(len(ppap)):
    if ppap[i] == "P":
        stack.append(ppap[i])
        continue
    # 불가능한 경우
    if len(stack) < 2 or i == len(ppap)-1:
        stack.append("A")
        break
    # PPAP면 => 앞에 PP 빼주기 & 마지막 PPAP면 앞에 값 빼주고 종료
    if ppap[i+1] == "P" and stack[-1] == "P" and stack[-2] == "P":
        stack.pop()
        stack.pop()
        if i == len(ppap)-2:
            break
    else:   # PPAP 성립 불가
        stack.append("A")
        break

# 스택에 값이 없거나 애초에 "P"였으면 => PPAP 문자열
if not stack or ppap =="P":
    flag = 0

if flag:
    answer = "NP"
else:
    answer = "PPAP"

print(answer)
