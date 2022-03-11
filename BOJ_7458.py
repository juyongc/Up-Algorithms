import sys
inputs = sys.stdin.readline


N = int(input())
A,B,C,D = [0]*N,[0]*N,[0]*N,[0]*N

for i in range(N):
    a,b,c,d = map(int,inputs().split())
    A[i],B[i],C[i],D[i] = a,b,c,d

AB = {}

# A,B 합 딕셔너리 만들기
for i in range(N):
    for j in range(N):
        ab = A[i] + B[j]
        if ab not in AB:
            AB[ab] = 1
        else:
            AB[ab] += 1

answer = 0
# C,D 합 구해서 AB에 -값 존재 확인
for i in range(N):
    for j in range(N):
        cd = C[i] + D[j]
        if -cd in AB:
            answer += AB[-cd]

print(answer)
