def solution(clothes):
    answer = 1
    category = dict()       # 딕셔너리
    # 모든 의상 확인
    for cloth in clothes:
        if cloth[1] not in category:        # 카테고리가 아직 없었으면
            category[cloth[1]] = 1
        else:                               # 존재하면
            now = category[cloth[1]] + 1    # 기존 수 + 1
            category[cloth[1]] = now
    
    for val in category.values():
        answer *= (val+1)   # 0도 가능하니까 (val+1)
    answer -= 1             # 안입는 케이스 제외
    return answer