N = int(input())

stars = [['*']*N for _ in range(N)]
n = 3   # 별 빼기 시작 크기
# n > N이면 break
while n <= N:
    # x,y => 전체 행,열 크기
    # n의 중간부터 별을 빼고, 빼고나면 n만큼 이동해서 반복
    for x in range(n//3,N,n):
        for y in range(n//3,N,n):
            # i,j는 빼야하는 별 개수
            for i in range(n//3):
                for j in range(n//3):
                    stars[x+i][y+j] = ' '
    n = n*3     # n 크기 3배수로 올리기

for i in range(N):
    print(''.join(stars[i]))