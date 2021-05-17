def tree(arr):

    tot = len(arr)//2 - 1
    nodes = list(set(arr[0:len(arr)-2]))    # 노드 번호 모으기
    utov = [0] * (tot + 1)                  # nodes 리스트 안에 있는 수 -> v
                                            # utov 리스트 안 => u
    # 빈 트리 => 트리
    if tot == 0:
        return 1
    # 노드 수 = 간선 수 + 1 => 트리
    if len(nodes) != tot+1:
        return 0
    # 한 노드에서 다른 노드 경로 = 1 로 유일 => 트리
    for k in range(tot):
        u = arr[2*k]
        v = arr[2*k+1]
        for j in range(tot+1):
            if nodes[j] == v:
                if utov[j] == 0:
                    utov[j] = u
                else:
                    return 0

    # 루트 개수 != 1 => 트리 아님
    cnt = 0         # 루트 개수 카운팅
    for k in range(tot+1):
        if utov[k] == 0:
            root = k
            cnt += 1
        # if cnt > 1:
        #     return 0
    if cnt != 1:
        return 0

    # 루트에서 모든 노드 다 갈 수 있는지 확인
    roots = [0]*(tot+1)     # 루트가 모든 노드 갈 수 있는지 체크리스트
    stack = [nodes[root]]   # 스택
    roots[root] = 1         # 루트 자리 체크
    while stack:
        now = stack.pop()
        for x in range(tot+1):
            if utov[x] == now and roots[x] == 0:
                roots[x] = 1
                stack.append(nodes[x])

    for k in range(len(roots)):
        if roots[k] == 0:
            return 0
    return 1


inputs = sys.stdin.readline
leap = []
b = []
while True:
    a = list(map(int,inputs().split()))
    if len(a) > 0:
        if a[-1] > 0:
            b += a
        elif a[-1] == 0:
            b += a
            leap.append(b)
            b = []
        else:
            break

num = len(leap)
for i in range(num):
    fin = tree(leap[i])
    if fin == 0:
        print('Case {0} is not a tree.'.format(i+1))
    else:
        print('Case {0} is a tree.'.format(i+1))