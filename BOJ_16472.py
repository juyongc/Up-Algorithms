import sys
inputs = sys.stdin.readline

N = int(input())
words = list(inputs().rstrip())

word_dict = {}
maxi = 0
word_cnt = 0
idx = 0
for i in range(len(words)):

    current = words[i]

    if current in word_dict:            # 이미 있는 문자열이면
        word_dict[current] += 1         # 현재값 딕셔너리에 +1
    else:                               # 처음 나온 문자열이면
        word_dict[current] = 1  # 현재값 딕셔너리에 +1
        word_cnt += 1

    # 투포인터 - 이전 문자열 LRU 인덱스 찾을 때까지 카운팅 개수 빼기
    while word_cnt > N:
        now = words[idx]
        if word_dict[now] == 1:
            word_cnt -= 1
            word_dict.pop(now)
        else:
            word_dict[now] -= 1
        idx += 1
    maxi = max(maxi, i - idx + 1)  # 최대값 갱신

print(maxi)