def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    
    # 이름으로 enroll의 인덱스 파악할 수 있게
    name_dict = {}
    for i in range(len(enroll)):
        name_dict[enroll[i]] = i

    cnt = 0     # seller 인덱스
    for sell in seller:
        money = amount[cnt] * 100
        name = sell
        # 이름이 "-" 아니면 계속 다음 추천인을 찾는다
        while name != "-":
            idx = name_dict[name]
            upload = money // 10
            answer[idx] += (money - upload)
            if upload < 1:      # 1원 미만이면 분배 stop
                break
            name = referral[idx]
            money = upload
        cnt += 1
    
    return answer