import sys
inputs = sys.stdin.readline

N = int(input())
tower = list(map(int,inputs().split()))

level = [[i+1,tower[i]] for i in range(N)]
stack = []
answer = [0]*N

# level에서 pop 해서 stack에 추가한다
# 추가하기 전에 stack에 값이 있으면 비교해서
# 추가될 값보다 작으면 pop하고 answer을 갱신한다
# 크면 break
# stack은 내림차순으로 만들어지기 때문
while level:
    now = level.pop()
    while stack:
        x = stack.pop()
        if now[1] >= x[1]:
            answer[x[0]-1] = now[0]
        else:
            stack.append(x)
            break
    stack.append(now)

print(" ".join(map(str,answer)))
