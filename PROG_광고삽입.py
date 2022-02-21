# 시간을 초단위로 환산
def convert_s(log_time):
    h,m,s = log_time.split(":")
    tot_s = int(h)*3600 + int(m)*60 + int(s)
    return tot_s

# 초단위를 구간으로 변환
def convert_period(h_num):
    
    h = h_num // 3600
    m_num = h_num % 3600
    m = m_num // 60
    s = m_num % 60
    if h < 10:
        h = "0{}".format(h)
    else:
        h = str(h)
    if m < 10:
        m = "0{}".format(m)
    else:
        m = str(m)
    if s < 10:
        s = "0{}".format(s)
    else:
        s = str(s)
    return "{}:{}:{}".format(h,m,s)


def solution(play_time, adv_time, logs):
    answer = 0
    play_conv = convert_s(play_time)
    adv_conv = convert_s(adv_time)
    period = [0]*(play_conv+2)
    # 로그 시작,끝점 초단위로 변환
    for log in logs:
        s_time = log[:8]
        e_time = log[9:]
        s_conv = convert_s(s_time)
        e_conv = convert_s(e_time)
        period[s_conv+1] += 1   # 시작+1 부터 ++
        period[e_conv+1] -= 1   # 끝+1 부터 --
    
    # 현재 시간 시청자 수
    watch = [0]*(play_conv+2)
    for i in range(1,play_conv+1):
        watch[i] = watch[i-1] + period[i]

    max_idx,max_t = 0,0     # max_시각, max_인원
    current = sum(watch[:adv_conv])
    max_t = current
    # 시청자 수 계산하기
    for i in range(adv_conv,play_conv+1):
        current += watch[i]
        current -= watch[i-adv_conv]
        if current > max_t:
            max_t = current
            max_idx = i-adv_conv
    answer = convert_period(max_idx)
    return answer