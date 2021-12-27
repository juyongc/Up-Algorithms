def solution(msg):
    answer = []
    # 기본 알파벳
    index = {"A":1,"B":2,"C":3,"D":4,"E":5,
              "F":6,"G":7,"H":8,"I":9,"J":10,
              "K":11,"L":12,"M":13,"N":14,"O":15,
              "P":16,"Q":17,"R":18,"S":19,"T":20,
              "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    cnt = 26    # 다음 인덱스 번호
    num = 0     # 메세지 인덱스 위치
    # 인덱스가 메세지 길이와 같거나 클때까지 반복
    while num < len(msg):
        letter = ""
        daum = 0
        while num+daum < len(msg):
            letter += msg[num+daum]
            if letter in index:     # 현재 글자가 사전에 있으면 다음 글자 추가
                daum += 1
            else:                   # 사전에 없으면 => 사전에 추가 / 이전 단어 정답에 추가
                cnt += 1
                num += daum
                index[letter] = cnt
                answer.append(index[letter[:len(letter)-1]])
                break
            # 메세지 길이보다 크면 => 현재 글자 추가 및 인덱스 위치 갱신    
            if num+daum >= len(msg):
                answer.append(index[letter])
                num += daum
                break
    return answer