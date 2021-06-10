import sys
from collections import deque
inputs = sys.stdin.readline

N = int(inputs())
tree = list(map(int,inputs().split()))
bye = int(inputs())

# 제거해야할 노드번호 넣기
q = deque()
q.append(bye)
# 제거해야할 노드의 자식노드 삭제 -> 해당 노드 "-2" 표시
# -1 은 부모 노드 고유로 남겨놔야 함
while q:
    now = q.popleft()
    tree[now] = -2
    for i in range(N):
        if tree[i] == now:
            q.append(i)

cnt = 0     # 리프 노드 카운트용

for i in range(N):
    if tree[i] != -2:           # 삭제된 노드가 아니면,
        ans = 0                 # 리프 노드 체크용
        for j in range(N):      
            if tree[j] == i:    # 자신의 자식이 있으면
                ans = 1         # 체크
                break
        if ans == 0:            # 리프 노드면
            cnt += 1            # 카운트

print(cnt)