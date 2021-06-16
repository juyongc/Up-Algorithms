# 점화식 이용 함수
def recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n % 2 == 1:
        return 1-recur(n//2)
    else:
        return recur(n//2)


k = int(input())
ans = recur(k-1)
print(ans)