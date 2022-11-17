import sys
inputs = sys.stdin.readline

# 몬스터와 전투 함수
# 몬스터보다 오래 살아남으면 => 용사 라이프 감소
# 아니면 => 용사 라이프 = 0
def fight(m_atk, m_life, h_atk, h_life):

    m_share, m_rem = divmod(m_life, h_atk)
    m_die = m_share
    if m_rem:
        m_die += 1
    h_share, h_rem = divmod(h_life, m_atk)
    h_die = h_share
    if h_rem:
        h_die += 1

    if m_die > h_die:
        h_life = 0
    else:
        h_life -= (m_atk * (m_die - 1))

    return h_life

# 포션 먹는 함수
# 공격력 증가, 생명력 => 최대 생명력 미만이면 증가
def heal(p_atk, p_life, h_atk, h_life, max_life):

    h_atk += p_atk
    h_life = min(h_life+p_life, max_life)

    return h_atk, h_life


N, start_atk = map(int,inputs().split())
rooms = [list(map(int,inputs().split())) for _ in range(N)]
s,e = 1, 10**18
answer = 10 ** 18

# 이분 탐색
while s <= e:
    mid = (s + e) // 2
    h_life = mid
    h_atk = start_atk
    flag = 0

    for room in rooms:
        option, o_atk, o_life = room
        if option == 1:     # 몬스터와 전투
            h_life = fight(o_atk,o_life,h_atk,h_life)
        else:               # 포션 먹기
            h_atk, h_life = heal(o_atk,o_life,h_atk,h_life, mid)
        
        if h_life <= 0:     # 용사 죽음
            flag = 1
            break
    # 상황별 이분탐색 기준 변화
    if flag:
        s = mid + 1
    else:
        answer = mid
        e = mid - 1

print(answer)
