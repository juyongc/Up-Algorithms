def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    now = 0
    # 정렬 후, B의 min과 A의 min값 비교
    # A의 min이 크면 A의 max 와 B min 대전
    for i in range(len(A)):
        if B[i] > A[now]:
            answer += 1
            now += 1
        else:
            A.pop()
    return answer