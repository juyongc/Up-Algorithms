import sys
inputs = sys.stdin.readline

N = int(input())
user_info = []

for _ in range(N):
    age,name = inputs().split()
    user_info.append((int(age),name))

user_info.sort(key= lambda x:x[0])  # 나이순으로만 정렬

for user in user_info:
    print(user[0],user[1])