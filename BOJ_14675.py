import sys

inputs = sys.stdin.readline

N = int(inputs())
node = [list() for _ in range(N+1)]
# 해당 node와 연결된 node를 node 리스트에 넣기
for _ in range(N-1):
    a,b = map(int,inputs().split())
    node[a].append(b)
    node[b].append(a)
q = int(inputs())
for _ in range(q):
    t,k = map(int,inputs().split())
    # 간선을 지우면 -> 무조건 그래프는 2개 이상
    if t == 2:
        print('yes')
    # 노드를 지우면
    # 해당 노드에 2개 이상 연결 -> 그래프 2개 이상
    # 해당 노드가 1개 연결 -> 그래프 1개('no' 출력)
    else:
        if len(node[k]) > 1:
            print('yes')
        else:
            print('no')
