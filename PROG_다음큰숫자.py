# 이진수에서 "1"개수 체크용
def bi_check(n):
    one = 0
    while n > 1:
        n,rem = divmod(n,2)
        if rem == 1:
            one += 1
    return one

def solution(n):
    answer = 0
    cur = n
    num = bi_check(cur)
    # n보다 큰 수 중에서
    # 이진화시, "1"의 개수 같은 수 찾기
    for i in range(n+1, 1000001):
        cnt = bi_check(i)
        if num == cnt:
            answer = i
            break
            
    return answer