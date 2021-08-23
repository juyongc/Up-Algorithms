from collections import deque


def solution(blen, mw, truck_weights):
    answer = 0
    tw = truck_weights
    q = deque()
    for i in range(blen):
        q.append(0)
    bridge = 0      # 다리 무게
    on_b = 0        # 다리 위 트럭 개수
    num = 0         # 다음 트럭 인덱스
    # 큐가 빌 때까지
    while q:
        now = q.popleft()   # now == 빠져나온 값
        bridge -= now       # 다리 무게 --
        if now != 0:        # 트럭이면 => 현 트럭 수 -1
            on_b -= 1
        # 남은 트럭이 있으면
        if num < len(truck_weights):
            # 다리에 트럭 수가 남으면 / 다음 트럭 올라가도 최대하중 안넘으면
            if on_b < blen and mw >= bridge + tw[num]:
                q.append(tw[num])   # 다음 트럭 ++
                bridge += tw[num]   # 다리 무게 ++
                on_b += 1           # 다리 위 트럭 수 ++
                num += 1            # 인덱스 ++
            else:
                q.append(0)
        answer += 1                 # 초 ++
    return answer
