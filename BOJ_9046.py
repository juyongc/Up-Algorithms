import sys

inputs = sys.stdin.readline

N = int(inputs())
for _ in range(N):
    words = inputs().rstrip()
    alpha = dict()          # 딕셔너리
    for word in words:      # 알파벳 체크
        if word == ' ':     # 빈칸이면 continue
            continue
        if word in alpha:   # 알파벳 딕셔너리에 있으면 => +1
            alpha[word] += 1
        else:               # 없으면 => 새로 만들기
            alpha[word] = 1
    maxi = 0        # max 값 초기화
    ans = ''        # 정답 알파벳 초기화
    for key,value in alpha.items():
        if value > maxi:        # 현재 max보다 크면 => 현재값으로 변경
            ans = key
            maxi = value
        elif value == maxi:     # 같으면 => 'ans = ?'
            ans = '?'
    print(ans)
