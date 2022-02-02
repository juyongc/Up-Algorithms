def solution(a):
    answer = 0
    if len(a) < 2:
        return answer
    check_num = {}
    visit = [[] for _ in range(len(a))]
    # 해당 인덱스는 이전 값, 이후 값과 비교 진행
    # 이전 값과 짝이 될 수 없다면 이후 값과 비교
    # 짝이 될 수 있으면 visit[이전] or visit[이후]에 (a[idx] 삽입 && check_num[a[idx]] ++)
    for i in range(len(a)):
        # 0번 인덱스 => 이후 값이랑만 비교
        if i == 0:
            if a[i] != a[i+1]:
                visit[i+1].append(a[i])
                check_num[a[i]] = 1
        # 마지막 인덱스 => 이전 값이랑만 비교
        elif i == (len(a) - 1):
            if a[i] != a[i-1] and a[i] not in visit[i-1]:
                visit[i-1].append(a[i])
                if a[i] not in check_num:
                    check_num[a[i]] = 1
                else:
                    check_num[a[i]] += 1
        else:
            if a[i] != a[i-1] and a[i] not in visit[i-1]:
                visit[i-1].append(a[i])
                if a[i] not in check_num:
                    check_num[a[i]] = 1
                else:
                    check_num[a[i]] += 1
            elif a[i] != a[i+1]:
                visit[i+1].append(a[i])
                if a[i] not in check_num:
                    check_num[a[i]] = 1
                else:
                    check_num[a[i]] += 1
    # 2개씩 짝이니까 max 값 구한 뒤, max값x2
    for key,val in check_num.items():
        answer = max(answer,val)
    answer *= 2
    return answer