def solution(cards):
    global visit
    
    answer = 0
    visit = [0]*(len(cards)+1)
    score = []
    # 모든 카드 dfs
    for i in range(len(cards)):
        if not visit[i]:
            val = dfs(cards,i)
            score.append(val)
            
    score.sort(reverse=True)
    if len(score) <= 1:
        answer = 0
    else:
        answer = score[0]*score[1]
        
    return answer

# 이미 열린 카드 걸릴때까지 확인
def dfs(cards,x):
    global visit
    stack = [cards[x]-1]
    cnt = 0
    while stack:
        now = stack.pop()
        if visit[now]:
            continue
        visit[now] = 1
        cnt += 1
        if now <= len(cards):
            stack.append(cards[now]-1)
        
    return cnt