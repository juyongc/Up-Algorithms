import sys
inputs = sys.stdin.readline

N = int(input())
word_dict = {}

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
for key,val in word_dict.items():
    value_list.append(val)

value_list.sort(reverse=True)

cnt = 9
for val in value_list:
    answer += (val*cnt)
    cnt -= 1

print(answer)
