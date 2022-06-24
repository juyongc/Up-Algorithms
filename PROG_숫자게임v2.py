def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    a_idx = 0
    # B값이 크면 => 승리 및 A의 다음 인덱스로 넘어가기
    for i in range(len(B)):
        if B[i] > A[a_idx]:
            answer += 1
            a_idx += 1
    
    return answer