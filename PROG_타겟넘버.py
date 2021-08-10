from collections import deque

def solution(numbers, target):
    answer = 0
    tot = len(numbers)
    if tot == 1:    # 주어진 리스트 크기가 1이면
        if numbers[0] == target:    # target과 같은지 체크
            answer = 1
    else:           # 크기가 1보다 크면
        answer += bfs(numbers, target)  # BFS
    return answer

# BFS 탐색
def bfs(nums,tar):
    cnt = 0         # target이랑 같은 값 카운팅
    tot = len(nums)
    q = deque()
    # 큐에 기본값 삽입
    q.append((nums[0],0))
    q.append((-nums[0],0))
    while q:
        val,cur = q.popleft()   # 현재값, 인덱스값
        if cur+1 >= tot:        # 리스트 크기 이상이면
            if val == tar:      # target이랑 같은지 체크
                cnt += 1
        else:                           # 리스트 크기보다 작으면
            plus = val + nums[cur+1]    # 다음값 각각 +/-한 값 구하고 append
            minus = val - nums[cur+1]
            q.append((plus,cur+1))
            q.append((minus,cur+1))
    return cnt