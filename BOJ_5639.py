import sys
inputs = sys.stdin.readline

prev = []
for line in sys.stdin:
    val = int(line.strip())
    prev.append(val)

tree = dict()
tree[prev[0]] = [0,0]
# 딕셔너리에 해당 노드 넣기
for i in range(1,len(prev)):
    cur = prev[i]
    if cur not in tree:
        tree[cur] = [0,0]
    now = prev[0]
    while True:
        if cur >= now:              # 현재값이 현노드보다 크면
            if tree[now][1] == 0:   # 1번 인덱스 확인 => 0이면 갱신
                tree[now][1] = cur
                break
            else:                   # 아니면 => 1번 인덱스와 비교
                now = tree[now][1]
        else:                       # 현재값이 현노드보다 작으면
            if tree[now][0] == 0:   # 0번 인덱스와 비교 => 0이면 갱신
                tree[now][0] = cur
                break
            else:                   # 아니면 => 비교
                now = tree[now][0]
s = [prev[0]]
answer = []
# 좌 - 우 순으로 append
# => pop()하면 반대니까
while s:
    nod = s.pop()
    answer.append(nod)
    x,y = tree[nod]
    if x != 0:
        s.append(x)
    if y != 0:
        s.append(y)

for i in range(len(answer)-1,-1,-1):
    print(answer[i])