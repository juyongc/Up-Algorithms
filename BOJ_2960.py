import sys

inputs = sys.stdin.readline

N,K = map(int,inputs().split())
num = [i for i in range(N+1)]   # 2~N 숫자 리스트
cnt,flag = 0,0                  # 카운팅 / break 플래그
# 2~N까지 반복
for i in range(2,N+1):
    if num[i] != 0:     # 0이 아니면
        p = num[i]      # 기준값
        x = 1           # 곱셈용
        now = p         # 현재값
        # N보다 작거나 같으면
        while now < N+1:
            if num[now] != 0:   # 아직 미방문이면
                num[now] = 0    # 방문 체크
                cnt += 1        # 카운팅 ++
                # K번째가 되면 => break 플래그 작동
                if cnt >= K:
                    ans = now
                    flag = 1
                    break
            x += 1          # 곱셈 +
            now = p * x     # 현재값 갱신
    # 플래그 작동했으면 => break
    if flag == 1:
        break

print(ans)