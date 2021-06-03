import sys

inputs = sys.stdin.readline

N,K,Q,M = map(int,inputs().split())
dozes = list(map(int,inputs().split()))
codes = list(map(int,inputs().split()))

# 코드 받은 학생과 조는 학생 중복 제거
for num in dozes:
    if num in codes:
        codes.remove(num)
        continue

# 방문 체크
attend = [0 for _ in range(N+3)]

# 코드 받은 학생 전체 체크
for stu in codes:
    fin = (N+2) // stu
    for i in range(1,fin+1):
        attend[stu*i] = 1

# 조는 학생 제외
for stu in dozes:
    attend[stu] = 0

# 해당 구간 못받은 학생 카운트
for k in range(M):
    f,e = map(int,inputs().split())
    cnt = 0

    for i in range(f,e+1):
        if attend[i] == 0:
            cnt += 1
    print(cnt)