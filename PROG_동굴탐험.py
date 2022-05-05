def solution(n, path, order):

    answer = False
    
    order_dict = {}
    for o in order:     # A->B 면, {B:A} 딕셔너리화
        order_dict[o[1]] = o[0]
    
    room = {}   # 노드별 방문가능한 노드 딕셔너리로 만들기
    for pa in path:
        r1,r2 = pa
        if r1 in room:
            room[r1].append(r2)
        else:
            room[r1] = [r2]
        if r2 in room:
            room[r2].append(r1)
        else:
            room[r2] = [r1]
            
    visit = [0]*n
    visit[0] = 1
    stack = [0]
    cnt = 0
    prev = {}
    while stack:
        now = stack.pop()
        # 순서가 있는데, 이전값을 방문못했으면 => prev에 딕셔너리 추가({A:B})
        if now in order_dict and visit[order_dict[now]] == 0:
            prev[order_dict[now]] = now
            continue
        
        visit[now] = 1
        cnt += 1
        
        for r in room[now]:
            if visit[r] == 0:
                stack.append(r)
        # 이전방문값이면 이후 방문값 추가
        if now in prev:
            stack.append(prev[now])
            
    if cnt == n:
        answer = True
    return answer