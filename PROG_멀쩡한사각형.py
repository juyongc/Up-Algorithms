# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(w,h):
    answer = w * h
    # 큰, 작은 수 정하기
    if w > h:
        small,big = h,w
    else:
        small,big = w,h

    nouse = gcd(small,big)
        
    return (answer - (w + h - nouse))