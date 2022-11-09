from itertools import combinations

def solution(beginning, target):
    global answer
    answer = 99999999
    
    current_coin = []   # 처음 동전 상태 복사용
    for i in range(len(beginning)):
        current = [0]*len(beginning[0])
        for j in range(len(beginning[0])):
            current[j] = beginning[i][j]
        current_coin.append(current)
        
    row = [i for i in range(len(beginning))]
    # row를 뒤집을 수 있는 모든 경우의 수
    for i in range(len(row)+1):
        row_com = list(combinations(row,i))
        val = flip(row_com,current_coin,target)
        answer = min(val,answer)
        
    if answer == 99999999:
        answer = -1
    return answer

# 주어진 row의 경우의 수를 뒤집고
# 모든 컬럼의 첫번째 값이 target과 다르면 뒤집는다
# 이후 타겟과 해당 컬럼값이 같은지 확인, 다르면 다음 row 경우의 수 비교
def flip(row_com,current_coin,target):
    global answer
    current_min = 99999999
    # 현재 row 조합의 모든 경우의 수
    for r_element in row_com:
        current_coin = row_flip(r_element,current_coin) 
        col = set()
        flag = 0
        # 첫번째 컬럼값이 다르면 뒤집기
        for x in range(len(current_coin[0])):
            if current_coin[0][x] != target[0][x]:
                current_coin = col_flip(x,current_coin)
                col.add(x)
                # 이미 정답보다 개수 많으면 => 백트래킹
                if len(r_element)+len(col) >= answer:
                    flag = 1
                    break
            # 타겟과 비교, 다르면 break
            for y in range(len(current_coin)):
                if current_coin[y][x] != target[y][x]:
                    flag = 1
                    break
            if flag:
                break
        # current_coin 원상복귀
        for c in list(col):
            current_coin = col_flip(c,current_coin)
        current_coin = row_flip(r_element,current_coin)
        # 모두 타겟과 같으면 => 현재 최소값 갱신
        if not flag:
            current_min = min(current_min,len(r_element)+len(col))
        
    return current_min

# 행 뒤집기
def row_flip(r_element,current_coin):
    
    for r in r_element:
        for k in range(len(current_coin[0])):
            if current_coin[r][k]:
                current_coin[r][k] = 0
            else:
                current_coin[r][k] = 1
    return current_coin

# 열 뒤집기   
def col_flip(c,current_coin):
    
    for k in range(len(current_coin)):
        if current_coin[k][c]:
            current_coin[k][c] = 0
        else:
            current_coin[k][c] = 1
    return current_coin