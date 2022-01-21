import sys
from itertools import combinations
inputs = sys.stdin.readline

word = list(input())
N = int(input())
major = []

for _ in range(N):
    price,name = list(inputs().split())
    price = int(price)
    major.append([price,name])

major.sort()
sum_major = []
for i in range(1,N+1):
    if i > len(word):
        break

    combi = list(combinations(major,i))
    for comb in combi:
        price = 0
        name = ''
        for com in comb:
            price += com[0]
            name += com[1]
        sum_major.append([price,name])

sum_major.sort()
answer = -1
for current in sum_major:
    flag = 0
    for alpha in word:
        if alpha in current[1]:
            current[1] = current[1].replace(alpha,"",1)
        else:
            flag = 1
            break
    if flag == 0:
        answer = current[0]
        break

print(answer)