def solution(skill, skill_trees):
    
    answer = 0
    check = set(skill)
    # 모든 스킬트리 확인
    for tree in skill_trees:
        cnt = 0     # 스킬 인덱스
        flag = 0    # 이상 여부 체크
        # 스킬트리 스킬 체크
        for alpha in tree:
            if alpha in check:      # 스킬트리 스킬이 스킬에 있으면
                if alpha != skill[cnt]: # 다음 스킬이 아니면 => 이상 체크
                    flag = 1
                    break
                else:               # 다음 스킬이 맞으면 => 다음 스킬 체크
                    cnt += 1
                    if cnt == len(skill):   # 모든 스킬 배웠으면 break
                        break
        if flag == 0:       # 문제 없으면 개수 ++
            answer += 1
    
    return answer