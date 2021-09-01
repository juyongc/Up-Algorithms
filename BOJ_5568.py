from itertools import permutations

N = int(input())
K = int(input())
nums = [input() for _ in range(N)]
# 모든 조합 구해서 set으로 중복 제거
tot = list(set(map(''.join,permutations(nums,K))))
print(len(tot))