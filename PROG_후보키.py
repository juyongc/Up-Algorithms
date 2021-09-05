from itertools import combinations as combi

def solution(relation):
    col = len(relation[0])
    row = len(relation)
    nums = [i for i in range(col)]
    candi = []
    # 모든 컬럼 조합 찾기
    for i in range(1,row+1):
        candi += list(combi(nums,i))
    
    right = []
    # 조합별 데이터 중복 확인
    for vals in candi:
        test = {}
        flag = 0
        for datas in relation:
            now = ''
            for val in vals:
                now += datas[val]
            if now in test:
                flag = 1
                break
            else:
                test[now] = 1
        # 통과했다면, 부분집합이 이미 존재하는지 확인
        if flag == 0:
            check = []
            for i in range(1,len(vals)+1):
                check += list(combi(vals,i))
            for may in right:
                if may in check:
                    break
            else:
                right.append(vals)
    answer = len(right)
                
    return answer