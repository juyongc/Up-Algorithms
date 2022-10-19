import sys
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
lamp = [list(inputs().rstrip()) for _ in range(N)]
K = int(input())

row_dict = {}

# 꺼진 램프 위치 같은 개수 구하기
for i in range(N):
    row = []
    for j in range(M):
        if lamp[i][j] == "0":
            row.append(j)
    tuple_row = tuple(row)
    if tuple_row in row_dict:
        row_dict[tuple_row] += 1
    else:
        row_dict[tuple_row] = 1

answer = 0
for key,val in row_dict.items():
    if K == 0:                  # K가 0이라면 => 꺼진 램프 개수가 0인 개수가 정답
        if len(key) == 0:
            answer = val
            break
    elif K % 2:                 # K가 홀수면 => 자신보다 작거나 같은 값중 꺼진 램프가 홀수인게 정답
        if len(key) <= K and len(key) % 2:
            answer = max(answer, val)
    else:                       # K가 짝수면 => 자신보다 작거나 같은 값중 꺼진 램프가 짝수인게 정답
        if len(key) <= K and len(key) % 2 == 0:
            answer = max(answer, val)

print(answer)
