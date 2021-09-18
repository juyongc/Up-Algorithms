A = input()
B = input()
# 긴/짧은 문자열 찾기
if len(A) > len(B):
    lg = A
    st = B
else:
    lg = B
    st = A
dp = [[0]*(len(lg)+1) for _ in range(len(st)+1)]    # dp용 리스트
# 같은 문자면 이전값 + 1
# 다른 문자면 비교후, max값 갱신
for i in range(1,len(st)+1):
    for j in range(1,len(lg)+1):
        if st[i-1] == lg[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])
