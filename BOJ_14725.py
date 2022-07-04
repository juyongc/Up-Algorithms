import sys
inputs = sys.stdin.readline

N = int(input())
tree = []
# 데이터 전부 넣기
for _ in range(N):
    tree_data = list(inputs().split())
    tree.append(tree_data[1:])

tree.sort()     # 트리 정렬

answer = []
dash = "--"
# 이전값이랑 비교해서 현재 트리의 개수가 더 크거나 
# 이전 트리의 인덱스와 현재 트리 인덱스의 값이 다르면 
# 비교를 멈추고, 인덱스부터 시작해서 모든 값을 넣는다
for i in range(N):
    if i == 0:      # 첫번째 값은 비교군이 없으니 다 넣기
        for j in range(len(tree[i])):
            answer.append(dash*j + tree[i][j])
        continue
    idx = 0         # 이전값과 다른 인덱스 찾기
    for j in range(len(tree[i])):
        if j >= len(tree[i-1]) or tree[i][j] != tree[i-1][j]:
            break
        idx += 1
    # 값이 다른 인덱스부터 모두 넣기
    for j in range(idx,len(tree[i])):
        answer.append(dash*j + tree[i][j])

for ans in answer:
    print(ans)
