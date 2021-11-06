import sys
inputs = sys.stdin.readline

# 현재 값 확인 후
# 해당 결과에 따라 4등분 or 값 반환
def check(x1, x2, y1, y2):
    s = plates[x1][y1]
    flag = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if plates[i][j] != s:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:
        a = check(x1, (x1 + x2) // 2, y1, (y1 + y2) // 2)
        b = check(x1, (x1 + x2) // 2, (y1 + y2) // 2, y2)
        c = check((x1 + x2) // 2, x2, y1, (y1 + y2) // 2)
        d = check((x1 + x2) // 2, x2, (y1 + y2) // 2, y2)
        cur = '(' + a + b + c + d + ')'
        return cur
    else:
        return str(s)


N = int(input())
plates = [list(inputs().rstrip()) for _ in range(N)]

ans = check(0,N,0,N)

print(ans)