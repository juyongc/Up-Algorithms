# N by N -> N//2 by N//2 행렬로 만드는 함수
def div(arr,num):
    global ans
    # 크기가 1이면 답이니까 저장 후 리턴
    if num == 1:
        ans = arr[0][0]
        return

    new = []        # N//2 by N//2 행렬 저장용
    for i in range(0,num,2):
        small = [0]*(num//2)        # 두번째로 큰 값만 모아서 행렬의 한 행 만들기
        for j in range(0,num,2):
            R = [0] * 4         # 2 by 2 행렬에서 값 추출하기
            R[0] = arr[i][j]
            R[1] = arr[i+1][j]
            R[2] = arr[i][j+1]
            R[3] = arr[i+1][j+1]
            R.sort()
            small[j//2] = R[2]  # 두번째로 큰 값 small에 저장
        new.append(small)       # small 행렬 값 다 만들었으면 new에 append
    div(new,num//2)             # div 재귀


N = int(input())
pulling = [list(map(int,input().split())) for _ in range(N)]
ans = 0         # 정답 저장용 변수
div(pulling,N)  # 함수 실행

print(ans)