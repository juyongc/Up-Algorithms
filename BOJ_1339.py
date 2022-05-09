import sys
inputs = sys.stdin.readline

N = int(input())
word_dict = {}  # {알파벳:값} 저장용

# 알파벳별 크기 측정
for _ in range(N):
    word = input()
    word = word[::-1]
    for i in range(len(word)):
        alpha = word[i]
        if alpha in word_dict:
            word_dict[alpha] += (10**i)
        else:
            word_dict[alpha] = (10 ** i)

answer = 0
value_list = []
# 값 큰 순서대로 정렬
for key,val in word_dict.items():
    value_list.append(val)

value_list.sort(reverse=True)

cnt = 9
# 9부터 값 배정
for val in value_list:
    answer += (val*cnt)
    cnt -= 1

print(answer)
