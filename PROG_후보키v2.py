from itertools import combinations
def solution(relation):
    global visit
    
    answer = 0
    N = len(relation[0])
    visit = []      # 찾은 후보키 저장 리스트
    
    # 개수별 모든 조합 찾기
    for i in range(1,N+1):
        key_list = list(combinations([k for k in range(1,N+1)],i))
        # 최소성 만족 확인
        for key in key_list:
            check = check_key(key)
            if check:
                continue
                
            duplicate = set()       # 중복 여부 확인용 set
            # 유일성 만족 확인
            for rel in relation:
                now = tuple(rel[val-1] for val in key)
                duplicate.add(now)
            # 최소성, 유일성 만족 => visit에 키 추가 & answer ++
            if len(duplicate) == len(relation):
                answer += 1
                visit.append(key)
    return answer


# 최소성 만족 확인 => True면 최소성 불만족
def check_key(key):
    global visit
    
    for j in range(1,len(key)+1):
        check_list = list(combinations(key,j))
        for ch in check_list:
            if ch in visit:
                return True
    
    return False