import sys
inputs = sys.stdin.readline

# dfs 탐색
def dfs(c,n,word):
    
    if c > N-2:             # 자음 최소 2개 포함
        return
    if len(word) == N:      # 암호 완성되면
        if c != 0:          # 모음 최소 1개 포함
            print(word)
        return

    for j in range(n+1,M):
        if letters[j] in col:
            dfs(c+1,j,word+letters[j])
        else:
            dfs(c, j, word + letters[j])


N,M = map(int,inputs().split())
letters = list(inputs().split())
letters.sort()      # 알파벳순

col = {'a':1,'e':1,'i':1,'o':1,'u':1}
num = 1
for i in range(M-N+1):
    cnt = 0     # 모음 카운팅용
    if letters[i] in col:
        cnt += 1
    now = letters[i]    # 현재 암호
    dfs(cnt,i,now)