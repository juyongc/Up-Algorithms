import sys
inputs = sys.stdin.readline

# kmp 함수
def kmp(s,p,table):

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]

        if s[i] == p[j]:
            j += 1

        if j == len(p):
            return 1

    return 0


s = inputs().rstrip()
p = inputs().rstrip()

table = [0]*len(p)  # 패턴에서 같은 문자열 체크

j = 0
for i in range(1,len(p)):
    while j > 0 and p[i] != p[j]:
        j = 0

    if p[i] == p[j]:    # 같으면 j ++ / table 갱신
        j += 1
        table[i] = j
ans = kmp(s,p,table)
print(ans)