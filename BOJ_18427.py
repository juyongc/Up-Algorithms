import sys
inputs = sys.stdin.readline

N,M,H = map(int,inputs().split())
student = [list(map(int,inputs().split())) for _ in range(N)]

dp = [[0]*(H+1) for _ in range(N)]

# 첫 학생 dp 만들기 => 가지고 있는 블럭 인덱스 1로 초기화
for stu in student[0]:
    dp[0][stu] = 1

# 모든 학생 dp 만들기
# 가지고 있는 블럭 +1
# 1~H까지 이전 학생이 들고 있던 값 ++
for i in range(1,N):
    for stu in student[i]:
        dp[i][stu] += 1
        for j in range(1,H+1):
            if dp[i-1][j]:
                if j+stu <= H:
                    dp[i][j+stu] += dp[i-1][j]
    # 앞에 가지고 있던 학생 블럭 정보 합치기
    for k in range(1,H+1):
        dp[i][k] += dp[i-1][k]

answer = dp[-1][-1] % 10007
print(answer)