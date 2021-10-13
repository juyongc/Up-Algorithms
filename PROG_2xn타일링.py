def solution(n):
    cnt = 3
    a,b = 1,2
    c = 3
    # dp 리스트 사용하면 => 시간초과남
    # a,b,c(i-2,i-1,i) 변수 사용해서 풀이
    while cnt < n:
        a,b = b,c
        c = a+b
        cnt += 1
    answer = c
    return (answer%1000000007)