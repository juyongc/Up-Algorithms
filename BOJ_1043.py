import sys
from collections import deque
inputs = sys.stdin.readline

N,M = map(int,input().split())
truth = list(map(int,inputs().split()))
truth.pop(0)
party = []
for _ in range(M):
    party_list = list(map(int,inputs().split()))
    party.append(party_list[1:])

person = {}                 # 사람별 소속한 파티 딕셔너리
for i in range(1,N+1):
    person[i] = []

for i in range(M):
    for p in party[i]:
        person[p].append(i)

visit_party = [0]*M             # 진실말한 파티 확인용(1)
visit_person = [0]*(N+1)        # 진실말한 사람 확인용(1)

stack = deque()                 # 진실말한 사람 추적용
for tru in truth:
    visit_person[tru] = 1
    stack.append(tru)

cnt = 0                         # 진실말한 파티 개수
while stack:
    now = stack.pop()           # 현재 추적중인 사람
    check = []                  # 추적중인 사람 소속된 "진실말할 예정인" 파티
    for val in person[now]:
        if visit_party[val] == 0:
            visit_party[val] = 1
            cnt += 1
            check.append(val)
    for c_val in check:         # 진실말할 예정인 파티에 속한 사람들 찾기
        for party_person in party[c_val]:
            if visit_person[party_person] == 0:
                stack.append(party_person)
                visit_person[party_person] = 1
answer = M - cnt
print(answer)