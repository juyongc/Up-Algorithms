import sys
inputs = sys.stdin.readline

N = int(input())
arr = list(map(int,inputs().split()))
arrow = {}      # 날아가고 있는 화살 높이 딕셔너리
answer = 0
for a in arr:
    if a in arrow:          # 화살 높이와 풍선 높이가 같다면
        if arrow[a] > 0:    # 화살 높이가 0보다 크면 => 풍선 터짐
            arrow[a] -= 1
        else:               # 현재 높이 화살이 이미 터져서 없다면
            answer += 1     # 화살 다시 쏴야 함
    else:                   # 현재 높이 화살이 없다면
        answer += 1         # 화살 추가

    # 화살 높이 - 1
    if a - 1 in arrow:      # 이미 존재하면 + 1
        arrow[a - 1] += 1
    else:                   # 아니면 1로 초기화
        arrow[a - 1] = 1

print(answer)