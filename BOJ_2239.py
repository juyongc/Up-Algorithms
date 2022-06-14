import sys
inputs = sys.stdin.readline

# 가로,세로,3x3 확인하기
# 가장 먼저 zero 개수만큼 도달한 게 정답
def dfs(zero, num):
    global sudoku, answer
    if num >= len(zero):
        for z in range(9):
            answer.append(sudoku[z][:])
        return
    if answer:
        return
    x, y = zero[num]
    zone = check_zone(x, y)
    for i in range(1, 10):
        if str(i) in sudoku[x]:
            continue
        elif str(i) in column[y]:
            continue
        elif str(i) in square[zone]:
            continue
        else:
            sudoku[x][y] = str(i)
            column[y][x] = str(i)
            square[zone].append(str(i))
            dfs(zero, num + 1)
            sudoku[x][y] = '0'
            column[y][x] = '0'
            square[zone].pop()


def check_zone(x, y):
    r = x // 3
    c = y // 3
    area = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    return area[r][c]


sudoku = [list(input()) for _ in range(9)]

zero = []
answer = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == "0":
            zero.append((i,j))

column = []
# 세로 통합하기
for i in range(9):
    col = [sudoku[j][i] for j in range(9)]
    column.append(col)

square = []
# 3x3 통합하기
ii = 0
while ii < 3:
    jj = 0
    while jj < 3:
        sq = []
        for i in range(3):
            for j in range(3):
                if str(sudoku[i+3*ii][j+3*jj]) != '0':
                    sq.append(str(sudoku[i+3*ii][j+3*jj]))
        square.append(sq)
        jj += 1
    ii += 1

dfs(zero, 0)
for i in range(9):
    print("".join(map(str,answer[i])))
