import sys
inputs = sys.stdin.readline

N = int(inputs())
words = dict()
# 딕셔너리에 단어 넣기
for _ in range(N):
    word = inputs().rstrip()
    val = len(word)
    # 해당 길이 단어가 있으면 -> 중복 확인
    if val in words:
        if word not in words[val]:
            words[val] += [word]
    else:
        words[val] = [word]
# 단어 길이별 알파벳 정렬 후 출력 
for i in range(51):
    if i in words:
        order = sorted(words[i])
        for j in range(len(order)):
            print(order[j])