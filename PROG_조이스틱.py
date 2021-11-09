def solution(name):
    answer = 0
    maxi = len(name) - 1
    for idx,nam in enumerate(name):
        # 커서 상/하 조절
        answer += min(ord(nam) - ord('A'), ord('Z') - ord(nam) + 1)
        now = idx + 1
        # 커서 좌/우 조절
        while now < len(name) and name[now] == 'A':
            now += 1
        if now == len(name):    # 끝까지 A로 가면 의미없음
            now = 0             # => 초기화
        maxi = min(maxi,idx + idx + len(name) - now)    
    answer += maxi
    return answer