# 매개변수 => 현 배열, 현재 배열 번호, 이전 값
def combi(arr,cnt,prev):
    if cnt >= M:
        print(' '.join(map(str,arr)))
        return
    for i in range(prev,N+1):
        arr[cnt] = i
        combi(arr,cnt+1,i)


N,M = map(int,input().split())
combi([0]*M,0,1)
