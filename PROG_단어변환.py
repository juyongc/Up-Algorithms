answer = 0      # 정답 global로 만들기

def solution(begin, target, words):
    global answer
    visit = [0]*len(words)
    
    # dfs 탐색
    def dfs(now,cnt,want):
        global answer
        
        if now == want:     # 원하는 단어 됐으면 => 최소값 확인
            if answer == 0:
                answer = cnt
            else:
                answer = min(answer,cnt)
            return
        
        for i in range(len(words)):
            if visit[i] != 0:   # 방문했으면 => continue
                continue
            diff = 0            # 다른 알파벳 개수
            word = words[i]
            # 현재 단어랑 비교할 단어 다른 알파벳 개수 확인
            for j in range(len(word)):
                if now[j] != word[j]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:       # 한개만 다르면 => dfs
                visit[i] = 1
                dfs(word,cnt+1,want)
                visit[i] = 0
        
    dfs(begin,0,target)
    return answer