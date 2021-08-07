def solution(dart):
    answer = 0
    logic = ['']*3      # 3자리 배열
    prev = 0            # 이전 위치
    loc = 0             # 배열 인덱스
    # 전체 검사해서 숫자면 이전값까지 잘라서 logic에 넣기
    for i in range(1,len(dart)-1):
        if dart[i].isdigit():
            if i-1 == prev:     # 10의 자리인지 체크
                continue
            else:
                logic[loc] = dart[prev:i]
                prev = i
                loc += 1
    logic[loc] = dart[prev:]
    points = [0]*3
    # 3번 반복
    for i in range(3):
        score = logic[i]
        real = ''
        for str1 in score:
            if str1.isdigit():      # 점수 확인
                real += str1
            elif str1.isalpha():    # 보너스 조건 확인
                real = int(real)
                if str1 == "D":
                    real = real ** 2
                elif str1 == 'T':
                    real = real ** 3
                points[i] = real
            else:                   # 옵션 조건 확인
                if str1 == "#":
                    now = -1 * points[i]
                else:
                    if i == 0:
                        now = 2 * points[i]
                    else:
                        now = 2 * points[i]
                        points[i-1] = 2 * points[i-1]
                points[i] = now 
    answer = sum(points)            # 점수 합산
    return answer