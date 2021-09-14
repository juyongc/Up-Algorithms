N,M = map(int,input().split())
trees = list(map(int,input().split()))
s, e = 0,max(trees)     # 시작,끝값
mini = 9999999999999    # 최소값
ans = 99999999999       # 정답
while True:
    mid = (s+e) // 2    # 중간값
    tot = 0             # 자른 트리 개수
    for tree in trees:
        if tree > mid:
            tot += (tree - mid)
            if tot > mini:  # mini 초과 => break
                break
    if tot > mini:      # mini보다 크고
        if tot >= M:        # M보다 크거나 같으면
            s = mid + 1     # 시작값 올리기
        else:               # M보다 작으면
            e = mid         # 끝값 내리기
    elif tot <= mini:   # mini보다 작거나 같고
        if tot >= M:        # M보다 크거나 같으면
            mini = tot      # mini,ans 갱신
            ans = mid
            s = mid + 1
        else:           # mini보다 크면
            e = mid
    if s >= e:      # 종료 조건
        break
print(ans)