import sys
inputs = sys.stdin.readline

N = int(input())
man = list(map(int,inputs().split()))
woman = list(map(int,inputs().split()))

m_plus,m_minus = [],[]      # 키큰원 남, 키작원 남
w_plus,w_minus = [],[]      # 키큰원 여, 키작원 여

# 키작원과 키큰원을 분리한다
for m in man:
    if m >= 0:
        m_plus.append(m)
    else:
        m_minus.append(m)
for w in woman:
    if w >= 0:
        w_plus.append(w)
    else:
        w_minus.append(w)

m_plus.sort()
m_minus.sort()
w_plus.sort()
w_minus.sort()
ans = 0
w_idx,m_idx = 0,len(m_plus)-1
# 여자 - 키작원, 남자 - 키큰원
while w_idx < len(w_minus) and m_idx >= 0:
    woman_now, man_now = w_minus[w_idx],m_plus[m_idx]
    if abs(woman_now) > man_now:    # 짝이 맞다면 => 정답 갱신, 키작원 인덱스 +1
        ans += 1
        w_idx += 1
    m_idx -= 1                      # 어떤 경우든 키큰원 -1

w_idx,m_idx = len(w_plus)-1,0
# 여자 - 키큰원, 남자 - 키작원
while m_idx < len(m_minus) and w_idx >= 0:
    woman_now, man_now = w_plus[w_idx],m_minus[m_idx]
    if abs(man_now) > woman_now:
        ans += 1
        m_idx += 1
    w_idx -= 1

print(ans)
