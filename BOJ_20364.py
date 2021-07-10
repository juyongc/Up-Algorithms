import sys

inputs = sys.stdin.readline
N,M = map(int,inputs().split())
wish = [int(inputs()) for _ in range(M)]
# 리스트 대신 set 사용
visit = set()

for i in range(M):
    want = wish[i]
    now = want

    ans = 0
    while now > 1:
        # 이미 다른 오리 땅이면 -> ans 갱신
        # 가장 처음 만난 땅이어야 해서 끝까지 가야한다
        if now in visit:
            ans = now
        now = now // 2
    
    if ans == 0:        # 해당 오리 땅이 됐으니, visit에 추가
        visit.add(want)
    print(ans)