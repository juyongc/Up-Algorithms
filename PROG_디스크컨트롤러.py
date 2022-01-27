import heapq
def solution(jobs):
    answer = 0
    task_given = []
    # 힙 구조로 만들기
    for job in jobs:
        heapq.heappush(task_given,job)
    working = []
    now = 0
    while True:
        # task_given에 값이 있고, 요청 시간 넘었으면 => working에 추가
        while task_given and task_given[0][0] <= now:
            value = heapq.heappop(task_given)
            heapq.heappush(working,[value[1],value[0]])
        if working:     # working에 값 있으면 => 요청 처리
            task_fin = heapq.heappop(working)
            now += task_fin[0]
            answer += (now - task_fin[1])
        else:           # 없으면 => 다음 요청 시간 넘어가기 or 정답 처리
            if task_given:
                now = task_given[0][0]
            else:
                answer = answer // len(jobs)
                break
    return answer