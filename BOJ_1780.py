import sys

#  현재 종이 사이즈. 시작 x값, 시작 y값
def cut(size,x,y):
    # 현재 사이즈가 1보다 작으면 -> return
    if size < 1:
        return

    standard = paper[x][y]      # 처음 종이값
    flag = 0                    # 체크용
    # 현 사이즈 종이값 체크용
    for i in range(x,x+size):
        for j in range(y,y+size):
            # 다른 종이값이 나왔다 -> flag 변경, break
            if paper[i][j] != standard:
                flag = 1
                break
        if flag == 1:
            break
    # flag == 0 => 종이값이 다 같다
    # 현재 종이값 카운팅 ++
    if flag == 0:
        value[standard] += 1
    # 종이값이 다른다 -> 한 사이즈 줄여서 반복
    else:
        for i in range(3):
            for j in range(3):
                cut(size//3,x+i*size//3,y+j*size//3)


inputs = sys.stdin.readline
N = int(inputs())
paper = [list(map(int,inputs().split())) for _ in range(N)]
value = {-1:0, 0:0,1:0}     # -1,0,1 개수 카운팅용 딕셔너리

cut(N,0,0)

print(value[-1])
print(value[0])
print(value[1])
