import sys
inputs = sys.stdin.readline


# 좋은 수열인지 체크
def isGood(seq):
    for k in range(1, len(seq) // 2 + 1):
        if seq[len(seq) - k:] == seq[len(seq) - (2 * k):len(seq) - k]:
            return False
    return True

# 수열 만들기
def findGood(seq,idx):
    global N,flag

    if flag == 1:
        return

    if idx == N:
        print(seq)
        flag = 1
        return

    for j in range(1,4):
        if isGood(seq+str(j)):
            findGood(seq+str(j),idx+1)


N = int(input())
flag = 0
findGood("1",1)

