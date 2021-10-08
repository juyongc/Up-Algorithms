def solution(people, limit):
    answer = 0
    people.sort()
    s,e = 0,len(people)-1
    # 가장 큰 값이랑 작은 값 비교
    # 합쳐서 limit보다 작으면 s,e 숫자 갱신
    # 아니면 가장 큰 값만 -1
    while s <= e:
        if people[s]+people[e] <= limit:
            s += 1
        e -= 1
        answer += 1
    return answer