t = int(input())
for _ in range(t):
    n = int(input())
    answer = "YES"
    flag = 0

    tree = [{} for _ in range(11)]  # 전화번호별 확인
    nums = [input() for _ in range(n)]
    for num in nums:
        tot = len(num)
        for i in range(1,tot+1):
            now = num[:i]   # 현재까지 번호
            if now not in tree[i]:  # 없으면
                if i == tot:        # 끝이면 인덱스 1번 => 0
                    tree[i][now] = [1,1]
                else:               # 끝 아니면 인덱스 1번 => 1
                    tree[i][now] = [1,0]
            else:           # 해당 번호가 있으면
                if i == tot:        # 끝이면 => 일관성 X
                    answer = "NO"
                    flag = 1
                    break
                else:       # 끝이 아니면
                    if tree[i][now][1] == 1:    # 딕셔너리 안이 끝이면
                        answer = "NO"           # => 일관성 X
                        flag = 1
                        break
                    else:                       # 아니면
                        tree[i][now][0] += 1    # => 인덱스 0번 +1
        if flag == 1:
            break
    print(answer)