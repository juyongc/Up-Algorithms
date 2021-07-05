# 매개변수 (마지막 숫자, 뽑을 개수, 현재 뽑은 개수, 숫자 배열)
def combi(n,tot,cnt,arr):
    # 현재 뽑은 개수가 M개라면 -> return
    if cnt >= tot:
        print(' '.join(map(str,arr)))
        return
    # 중복없이 고르기
    for i in range(1,n+1):
        arr[cnt] = i
        combi(n,tot,cnt+1,arr)


N,M = map(int,input().split())
combi(N,M,0,[0]*M)