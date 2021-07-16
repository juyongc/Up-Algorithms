import sys

inputs = sys.stdin.readline
N,M = map(int,inputs().split())
given = {inputs().rstrip() for _ in range(N)}   # 딕셔너리에 주어진 문자열 넣기
cnt = 0     # 포함된 문자열 카운트용
# M만큼 반복
for _ in range(M):
    word = inputs().rstrip()    # 체크할 문자열
    if word in given:           # 딕셔너리에 있으면 -> cnt ++
        cnt += 1

print(cnt)