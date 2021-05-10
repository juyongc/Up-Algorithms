def queen(num):
    global cnt
    # 행이 N 이상이면 -> 모든 퀸 사용
    if num > N-1:
        cnt += 1
        return

    row[num] = 1
    # i -> 열 번호
    # num-i+(N-1) -> 왼쪽에서 오른쪽 대각선 번호
    # num+i -> 오른쪽에서 왼쪽 대각선 번호
    for i in range(N):
        if col[i] == 0 and dia_l[num-i+(N-1)] == 0 and dia_r[num+i] == 0:
            col[i] = 1
            dia_l[num-i+(N-1)] = 1
            dia_r[num+i] = 1
            queen(num+1)
            row[num] = 0
            col[i] = 0
            dia_l[num-i+(N-1)] = 0
            dia_r[num+i] = 0


N = int(input())
row = [0]*N             # 행
col = [0]*N             # 열
dia_l = [0]*(2*N-1)     # 왼쪽에서 오른쪽 대각선
dia_r = [0]*(2*N-1)     # 오른쪽에서 왼쪽 대각선
cnt = 0     # 카운트
queen(0)

print(cnt)