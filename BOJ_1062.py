import sys
from itertools import combinations
inputs = sys.stdin.readline

# 필요한 알파벳 중 num개를 뽑아서 반환
def getcombi(alphabet, num):

    if num < 0:                     # 0보다 작으면 불가능
        return []
    elif len(alphabet) <= num:      # 알파벳 개수가 num보다 작으면 combinations 사용 불가 - 필요한 알파벳 바로 반환
        return list(combinations(alphabet, len(alphabet)))
    else:                           # num개 뽑아서 리스트 반환
        return list(combinations(alphabet, num))

# 모든 combination에서 각각 모든 단어 중 몇 개가 가능한 지 파악
# 최대 count된 개수 반환
def check_all(word_set,combi):

    max_count = 0
    for comb in combi:
        count = 0
        for ws in word_set:
            flag = 1
            for w in ws:
                if w not in comb:
                    flag = 0
                    break
            if flag:
                count += 1
        if count > max_count:
            max_count = count

    return max_count


N,M = map(int,inputs().split())
word_list = [input() for _ in range(N)]
already = {"a","n","t","i","c"}
alphabet = set()

word_set = [set() for _ in range(N)]

cnt = -1
# 단어별 필요한 알파벳 구하기 & 모든 필요한 알파벳 set 구하기
for word in word_list:
    cnt += 1
    for i in range(4,len(word)-4):
        if word[i] in already:
            continue
        elif word[i] in alphabet:
            word_set[cnt].add(word[i])
            continue
        else:
            alphabet.add(word[i])
            word_set[cnt].add(word[i])


answer = 0
combi = getcombi(alphabet,M-5)

if combi:       # 콤비네이션 개수가 0이 아니면
    num = check_all(word_set,combi)
    if num > answer:
        answer = num

print(answer)
