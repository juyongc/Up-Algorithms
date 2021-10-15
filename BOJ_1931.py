import sys
inputs = sys.stdin.readline

N = int(input())
convs = [tuple(map(int,inputs().split())) for _ in range(N)]
convs.sort()
cnt = 1     # 개수 카운팅
now = 0     # 현재 인덱스
flag = 0    # 끝 신호
# 모든 인덱스 탐색까지
while now < N:
    s,e = convs[now][0],convs[now][1]
    # 다음 회의실 찾기
    for j in range(now+1,N+1):
        if j == N:      # 끝까지 다 찾음
            flag = 1
            break
        ns,ne = convs[j][0],convs[j][1]
        if ns >= e:     # 현재 회의 끝났으면 => 다음 회의임
            now = j
            cnt += 1
            break
        elif ne < e:    # 현재 회의보다 먼저 끝나면 => 그냥 교체
            now = j
            break
    if flag == 1:
        break

print(cnt)
