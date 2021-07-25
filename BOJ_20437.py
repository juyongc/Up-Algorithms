import sys

inputs = sys.stdin.readline
T = int(inputs())
for _ in range(T):
    alpha = inputs().rstrip()
    N = int(inputs())
    check = dict()      # 알파벳 체크용 dictionary
    mini = 1000000      
    maxi = 0
    word_length = len(alpha)
    # 문자열 문자 개수만큼 반복
    for i in range(word_length):
        cur = alpha[i]              # cur = 현재 알파벳
        if cur not in check:        # 현재 알파벳이 없었다면
            check[cur] = [i]
            if N == 1:              # N == 1 고려
                mini,maxi = 1,1
        else:                       # 알바벳이 존재하면
            check[cur] += [i]       # 기존 key에 value 추가
            cur_length = len(check[cur])
            if cur_length >= N:     # 현재 개수가 N보다 크면,
                val = check[cur][cur_length - 1] - check[cur][cur_length - N] + 1
                # max,min 계산
                if val > maxi:
                    maxi = val
                if val < mini:
                    mini = val
    if mini == 1000000 and maxi == 0:   # 연속 문자열 없었으면
        print(-1)
    else:                               # 있으면
        print(mini,maxi)
