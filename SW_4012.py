def div(x,k):
    global num
    # stack에 A 음식 조합 배열 넣기
    if x == N//2:
        stack.append(A[:])
        num -= 1
        return
    # A 조합 다 들어갔으니 함수 빠져 나오기
    if num == 0:
        return
    # 조합 구하기
    for i in range(k,N):
        if visit[i] == 0:
            A[x] = i
            visit[i] = 1
            div(x+1,i)
            visit[i] = 0


for t in range(1,T+1):
    N = int(input())
    food = [list(map(int,input().split())) for _ in range(N)]
    visit = [0]*N
    mini = 999999
    stack = []
    A = [0]*(N//2)
    # 조합 개수 구하기
    num = 1
    for i in range(N//2):
        num *= (N-i)
        num //= (i+1)
    num = num // 2
    # 모든 A 조합 구하는 함수 
    div(0,0)
    # A,B 음식 맛 차이 최소 구하기
    while stack:
        C1 = stack.pop()
        C2 = []
        for i in range(N):
            if i not in C1:
                C2.append(i)

        eat1,eat2 = 0,0

        for i in range(N//2):
            for j in range(N//2):
                if i != j:
                    eat1 += food[C1[i]][C1[j]]
                    eat2 += food[C2[i]][C2[j]]

        diff = abs(eat2 - eat1)

        if diff < mini:
            if diff == 0:
                mini = 0
                break
            else:
                mini = diff

    print('#{} {}'.format(t,mini))