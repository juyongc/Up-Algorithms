import sys

# 이분탐색 함수
def guess(num):
    now = given[num]
    l = 0           # 시작점
    h = N-1         # 종료점
    m = (l+h)//2    # 중간값
    # 주어진 수랑 같은 카드가 있으면 stop
    while now != my[m]:
        # 주어진 수가 해당 수보다 크면,
        if now > my[m]:
            l = m+1     # 다음 시작지점은 m+1
        # 주어진 수가 해당 수보다 작으면,
        elif now < my[m]:
            h = m-1     # 다음 종료지점은 m-1

        m = (l + h) // 2    # 중간값 계산
        # 시작점이 종료점보다 크거나
        # 종료점이 시작점보다 작으면 return
        if l > h:
            return
        if h < l:
            return
        
    # 해당 인덱스 체크
    check[num] = 1
    return


inputs = sys.stdin.readline
N = int(inputs())
my = list(map(int,inputs().split()))
M = int(inputs())
given = list(map(int,inputs().split()))

check = [0]*M       # check용
my.sort()           # 이분탐색용 sort

# M만큼 반복
for i in range(M):
    # 주어진 수가 상근이 카드 최소,최대보다 작거나 크면 continue
    if given[i] < my[0] or given[i] > my[-1]:
        continue
    # 아니면 이분탐색
    else:
        guess(i)

print(' '.join(map(str,check)))