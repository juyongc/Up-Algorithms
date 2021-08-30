from itertools import permutations as permu


def solution(numbers):
    every = []
    # 모든 순열 찾기
    for i in range(1, len(numbers) + 1):
        every += list(permu(numbers, i))
    every = list(set(every))    # 중복 제거
    candidate = []  # int값 담을 리스트
    # 각 튜플을 문자열로 만든후, int 변환
    for num in every:
        now = ''
        for val in num:
            now += val
        candidate.append(int(now))
    candidate = list(set(candidate))    # 중복 제거
    cnt = 0     # 소수 카운팅용
    for candi in candidate:
        if candi == 0 or candi == 1:    # 0,1은 제외
            continue
        flag = 0    # 소수인지 체크
        for i in range(2, candi):
            if candi % i == 0:  # 나눠떨어지면 소수 아님
                flag = 1
                break
        if flag == 0:   # 소수면 => 카운팅 ++
            cnt += 1

    return cnt