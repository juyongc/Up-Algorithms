import sys
inputs = sys.stdin.readline


def findAnswer(ff,fs,sf,ss):
    num = 0
    # 빠른 시작 없으면 => ss + 최대 sf 1번
    if ff == 0 and fs == 0:
        num += ss + min(sf,1)
        return num
    # fs == 0이면, ff만 가능
    if fs == 0:
        num += ff
        return num
    # fs는 sf보다 1번 더 많이 할 수 있음
    # sf는 fs보다 많이 할 수 없음
    if fs > sf:
        num += ff + ss + 2 * sf + 1
    else:
        num += ff + ss + 2 * fs

    return num


ff,fs,sf,ss = map(int,inputs().split())
answer = findAnswer(ff,fs,sf,ss)
print(answer)
