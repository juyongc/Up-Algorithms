import sys


def combi(cnt):
    # 리스트 다 찼으니 출력 후 return
    if cnt >= M:
        print(' '.join(map(str,arr)))
        return

    for i in range(N):
        # 방문 안했으면
        if visit[i] == 0:
            arr[cnt] = nums[i]      # 해당 숫자 저장
            visit[i] = 1            # 방문 체크
            combi(cnt+1)            # 다음 인덱스로 넘어감
            visit[i] = 0            # 방문체크 해제


inputs = sys.stdin.readline
N,M = map(int,inputs().split())
# 주어진 수 -> 사전순으로 나오게 sort
nums = list(map(int,inputs().split()))
nums.sort()
arr = [0]*M     # 숫자값 저장 리스트
visit = [0]*N   # 방문체크용

combi(0)