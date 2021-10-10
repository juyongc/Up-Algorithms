def solution(win_nums, lottos):
    answer = [6,6]
    cnt = 0
    same = 0
    score = 0
    # 당첨 여부 / 낙서 개수 찾기
    for j in range(len(win_nums)):
        if win_nums[j] == 0:
            cnt += 1
            continue
        for i in range(len(lottos)):
            if win_nums[j] == lottos[i]:
                same += 1
                break
    maxi = same + cnt
    mini = same
    # 순위 정하기
    for i in range(6,1,-1):
        if maxi == i:
            answer[0] = 6 - i + 1
        if mini == i:
            answer[1] = 6 - i + 1

    
    return answer