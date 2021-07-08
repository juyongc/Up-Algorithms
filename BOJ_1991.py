import sys

# 전위 순회
def pre(now):

    for i in range(N):
        if get_node[i][0] == now:
            cur = get_node[i]
            break
    # 현재 출력 -> 왼쪽 자식 탐색 -> 오른쪽 자식 탐색
    print(now,end='')
    if cur[1] != '.':
        pre(cur[1])
    if cur[2] != '.':
        pre(cur[2])

# 중위 순회
def inorder(now):

    for i in range(N):
        if get_node[i][0] == now:
            cur = get_node[i]
            break
    # 왼쪽 자식 탐색 -> 출력 -> 오른쪽 자식 탐색
    if cur[1] != '.':
        inorder(cur[1])
    print(now,end='')
    if cur[2] != '.':
        inorder(cur[2])

# 후위 순회
def post(now):

    for i in range(N):
        if get_node[i][0] == now:
            cur = get_node[i]
            break
    # 왼쪽 자식 탐색 -> 오른쪽 자식 탐색 -> 출력
    if cur[1] != '.':
        post(cur[1])
    if cur[2] != '.':
        post(cur[2])
    print(now, end='')


inputs = sys.stdin.readline

N = int(inputs())
get_node = [list(inputs().split()) for _ in range(N)]

pre('A')
print()
inorder('A')
print()
post('A')
