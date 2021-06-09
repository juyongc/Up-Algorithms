import sys

inputs = sys.stdin.readline

N,M = map(int,inputs().split())
words = ['']*N
for i in range(N):
    words[i] = inputs().rstrip()

alpha = 'ACGT'
check = [[0]*4 for _ in range(M)] # 자리 수별 해당 알파벳 개수 체크

# 자리 수별 해당 알파벳 개수 체크
for word in words:
    for m in range(M):
        if word[m] == 'A':
            check[m][0] += 1
        elif word[m] == 'C':
            check[m][1] += 1
        elif word[m] == 'G':
            check[m][2] += 1
        else:
            check[m][3] += 1

max_word = ''

# 자리 수별 가장 많은 알바벳 찾기
# 같으면 앞에 나온 알바벳이 우선순위
for i in range(M):
    maxi = 0
    pick = ''
    for j in range(4):
        if check[i][j] > maxi:
            maxi = check[i][j]
            pick = alpha[j]
    max_word += pick

cnt = 0
# 단어별 max_word랑 같은 위치, 다른 알파벳 개수 카운트 
for word in words:
    for m in range(M):
        if word[m] != max_word[m]:
            cnt += 1

print(max_word)
print(cnt)