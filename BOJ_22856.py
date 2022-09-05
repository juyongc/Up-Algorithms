import sys
inputs = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 중위 순회
def inorder(tree,now):

    if tree[now][0] != -1:
        inorder(tree,tree[now][0])
    inorder_list.append(now)
    if tree[now][1] != -1:
        inorder(tree,tree[now][1])

# 유사 중위 순회
def inorder_similar(tree,now,last):

    if tree[now][0] != -1:
        similar_list.append(now)
        inorder_similar(tree,tree[now][0],last)
    similar_list.append(now)
    # 중위 순회 마지막 값과 같으면 return
    if now == last:
        return
    if tree[now][1] != -1:
        inorder_similar(tree,tree[now][1],last)
        similar_list.append(now)


N = int(input())
tree = [[] for _ in range(N+1)]

for  _ in range(N):
    a,b,c = map(int,inputs().split())
    tree[a].append(b)
    tree[a].append(c)

inorder_list = []
inorder(tree,1)
last = inorder_list[-1]

similar_list = []
inorder_similar(tree,1,last)

cnt = 0
# 가장 마지막에 나온 중위 순회 마지막 값 이전까지가 답
# 자식 노드 모두 방문하는 게 우선순위가 높기 때문
for i in range(len(similar_list)-1,-1,-1):
    if similar_list[i] == last:
        cnt = i
        break

print(cnt)