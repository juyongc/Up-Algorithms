import sys
from collections import deque
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
students = [0]*(N+1)    # 자신과 연결된 간선 수 체크용
height = {}             # 자신보다 큰 학생 확인용
# 간선 수 갱신
for _ in range(M):
    A,B = map(int,inputs().split())
    students[B] += 1
    if A not in height:
        height[A] = [B]
    else:
        height[A].append(B)

# 가장 작은 학생들 찾기
q = deque()
for i in range(1,N+1):
    if students[i] == 0:
        q.append(i)

ans = []
# 큐에서 값 꺼낸뒤, 연결된 간선 갱신하고 
# 0이 되면 큐에 넣기
while q:
    num = q.popleft()
    ans.append(num)
    if num not in height:
        continue
    for val in height[num]:
        students[val] -= 1
        if students[val] == 0:
            q.append(val)

print(' '.join(map(str,ans)))