# ans_id: 저장된 가능한 조합 / pos_ids: 밴한 아이디별로 가능한 유저 아이디 /
# n: 밴 아이디 개수 / m: 현재 조사중인 인덱스 / 
# combi: 현재 구하는 조합 / visit: 방문 체크
def dfs(ans_id,pos_ids,n,m,combi,visit):

    if m >= n:  # 다 구했으면
        now = sorted(combi)     # sort 후, 문자열로 변환
        now = ''.join(map(str,now))
        if now not in ans_id:   # 중복 체크
            ans_id.add(now)
        return
    # dfs 구하기
    for pos in pos_ids[m]:
        if visit[pos] == 0:
            visit[pos] = 1
            combi[m] = pos
            dfs(ans_id,pos_ids,n,m+1,combi,visit)
            visit[pos] = 0

            
def solution(user_id, banned_id):
    answer = 0
    # 밴한 아이디별 가능한 유저 아이디 저장용
    pos_ids = [[] for _ in range(len(banned_id))]
    # 밴한 아이디별로 가능한 유저 아이디 구하기
    for i in range(len(banned_id)):     # 밴 아이디별로
        ban = banned_id[i]
        for j in range(len(user_id)):   # 모든 유저 아이디
            user = user_id[j]
            flag = 0
            if len(user) == len(ban):   # 밴 아이디와 유저 아이디 같은지 확인
                for k in range(len(ban)):
                    if ban[k] == '*':
                        continue
                    if ban[k] != user[k]:
                        flag = 1
                        break
                if flag == 0:
                    pos_ids[i].append(j)
    ans_id = set()              # 가능한 밴 아이디 조합 저장용
    combi = [-1]*len(banned_id) # 밴한 아이디 조합용
    visit = [0]*len(user_id)   # 방문 체크용 
    
    dfs(ans_id,pos_ids,len(banned_id),0,combi,visit)    # DFS
    answer = len(ans_id)
    
    return answer