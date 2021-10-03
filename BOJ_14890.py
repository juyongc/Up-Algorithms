import sys
inputs = sys.stdin.readline

N,L = map(int,inputs().split())
roads = [list(map(int,inputs().split())) for _ in range(N)]

cnt = 0
# 같은 행
for i in range(N):
    now = roads[i]
    visit = [0] * N
    for j in range(N):
        s = j
        flag = 0
        lin = 0
        for k in range(1,L+1):
            if s - k < 0:
                if lin == 1:
                    flag = 1
                break

            if now[s] - now[s-k] == 0 or now[s] - now[s-k] == -1:      # 같은 층
                if lin == 1:
                    flag = 1
                break
            elif now[s] - now[s-k] == 1:    # 한 층 차이
                if visit[s-k] == 1:         # 이미 설치했으면
                    flag = 1
                    break
                else:                       # 설치 X면
                    visit[s-k] = 1
                    lin = 1
            else:
                flag = 1
                break

        if flag == 1:
            break
        lin = 0
        for k in range(1,L+1):
            if s + k >= N:
                if lin == 1:
                    flag = 1
                break

            if now[s] - now[s+k] == 0 or now[s] - now[s+k] == -1:      # 같은 층
                if lin == 1:
                    flag = 1
                break
            elif now[s] - now[s+k] == 1:    # 한 층 차이
                if visit[s+k] == 1:         # 이미 설치했으면
                    flag = 1
                    break
                else:                       # 설치 X면
                    visit[s+k] = 1
                    lin = 1
            else:
                flag = 1
                break

        if flag == 1:
            break
    if flag == 0:
        cnt += 1
# 같은 열
for i in range(N):
    visit = [0] * N
    for j in range(N):
        now = roads[j][i]
        s = roads[j][i]
        flag = 0
        lin = 0
        for k in range(1,L+1):
            if j - k < 0:
                if lin == 1:
                    flag = 1
                break

            if s - roads[j-k][i] == 0 or s - roads[j-k][i] == -1:      # 같은 층
                if lin == 1:
                    flag = 1
                break
            elif s - roads[j-k][i] == 1:    # 한 층 차이
                if visit[j-k] == 1:         # 이미 설치했으면
                    flag = 1
                    break
                else:                       # 설치 X면
                    visit[j-k] = 1
                    lin = 1
            else:
                flag = 1
                break

        if flag == 1:
            break
        lin = 0
        for k in range(1,L+1):
            if j + k >= N:
                if lin == 1:
                    flag = 1
                break

            if s - roads[j+k][i] == 0 or s - roads[j+k][i] == -1:      # 같은 층
                if lin == 1:
                    flag = 1
                break
            elif s - roads[j+k][i] == 1:    # 한 층 차이
                if visit[j+k] == 1:         # 이미 설치했으면
                    flag = 1
                    break
                else:                       # 설치 X면
                    visit[j+k] = 1
                    lin = 1
            else:
                flag = 1
                break

        if flag == 1:
            break

    if flag == 0:
        cnt += 1
print(cnt)
