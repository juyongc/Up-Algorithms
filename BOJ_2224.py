import sys
from collections import deque

# A-Z,a-z 반복
# 방문체크해서 'start' => 'visited' 저장
def check(s):
    visit = [0]*52
    q = deque()
    q.append(s)
    visit[s] = 1        # 자기 자신은 제외(q에 추가로 안들어가게 미리 체크)
    while q:
        now = q.popleft()
        for num in arr[now]:
            if visit[num] == 0:
                q.append(num)
                visit[num] = 1
    visit[s] = 0        # 자기 자신은 제외
    for k in range(52):
        if visit[k] == 1:
            ans.append((alpha[s],alpha[k]))


inputs = sys.stdin.readline
X = int(inputs())
# 알파벳 문자열 위치(숫자 이용)
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

arr = [[] for _ in range(52)]
for _ in range(X):
    prop = inputs()
    a,b = prop[0],prop[5]
    # 처음, 마지막 문자열 숫자로 변환
    for i in range(52):
        if a == alpha[i]:
            a = i
        if b == alpha[i]:
            b = i
    arr[a].append(b)
# A-Z,a-z로 결과 나오게 sort 해주기
for i in range(52):
    arr[i].sort()

ans = []    # 정답 담을 리스트
for i in range(52):
    check(i)

print(len(ans))
for i in range(len(ans)):
    print('{0} => {1}'.format(ans[i][0],ans[i][1]))
