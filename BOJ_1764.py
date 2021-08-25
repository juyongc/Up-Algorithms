import sys

inputs = sys.stdin.readline
N,M = map(int,inputs().split())
heard = dict()
# 못들어본 사람 딕셔너리 만들기
for _ in range(N):
    name = inputs().rstrip()
    heard[name] = 1
cnt = 0     # 못듣, 못본 사람 카운팅
names = []  # 못든, 못본 사람 리스트

for _ in range(M):
    name = inputs().rstrip()
    if name in heard:       # 못본 사람 이름이 딕셔너리에 있으면
        cnt += 1            # 카운팅 ++
        names.append(name)  # 리스트에 추가
        
names.sort()    # 사전순 정렬
print(cnt)
for name in names:
    print(name)