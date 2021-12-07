import sys
inputs = sys.stdin.readline

N = int(input())

ans = []    # +,- 저장용
check = 0   # 정답 유무 확인용
s = []      # 스택
num = 1     # 현재 숫자
for _ in range(N):
    x = int(input())
    # input값이 num보다 크거나 같으면 => num ++ / "+" 추가
    while x >= num:
        s.append(num)
        ans.append("+")
        num += 1

    if x == s[-1]:  # 스택 마지막값과 비교
        s.pop()     # => 같으면 pop / "-" 추가
        ans.append("-")
    else:
        check = 1
        break

# 정답 확인 후, 조건따라 출력
if check == 1:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])