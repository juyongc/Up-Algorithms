def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    # A의 최소와 B의 최대를 곱함
    for i in range(len(A)):
        answer += (A[i]*B[i])
        
    return answer