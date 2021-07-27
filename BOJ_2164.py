import sys
from collections import deque

inputs = sys.stdin.readline
N = int(inputs())
q = deque()
# 큐에 1~N까지 넣기
for i in range(1,N+1):
    q.append(i)
# q가 빌때까지
# 첫번째 카드 버리고 두번째 카드는 뒤로 보내기
while q:
    ans = q.popleft()
    if not q:
        break
    else:
        ans = q.popleft()
        q.append(ans)
print(ans)
