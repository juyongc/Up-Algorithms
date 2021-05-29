# 이분탐색 
def sroot(s,e,q):
    global ans
    # 더이상 나눌 수 없는 s,e 사이가 답이라면,
    # 답은 e임
    if s == e-1:
        ans = e
        return
    
    m = (s+e)//2        # 중간값
    # 상황별 조건
    if m*m > q:
        sroot(s,m,q)
    elif m*m < q:
        sroot(m,e,q)
    else:
        ans = m
        return

# 메인
N = int(input())

if N*N == 0:        # 답이 0이면
    ans = N
elif N*N == N:      # 답이 1이면
    ans = N
else:               # 그 외
    sroot(0,N,N)

print(ans)