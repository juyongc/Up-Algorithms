import sys
inputs = sys.stdin.readline

total = 0
tree_dict = {}
tree_list = []
while True:
    tree = inputs().rstrip()
    if not tree:
        break
    total += 1
    if tree not in tree_dict:
        tree_dict[tree] = 1
        tree_list.append(tree)
    else:
        tree_dict[tree] += 1

tree_list.sort()
for name in tree_list:
    cnt = tree_dict[name]
    percent = round(cnt/total*100,4)
    print("{} {:.4f}".format(name,percent))