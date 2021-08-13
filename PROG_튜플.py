def solution(s):
    answer = []
    flag = 0    # 집합 시작 플래그
    now = ''    # 숫자 하나 크기
    # 각 조건별 숫자자르기 / 삽입
    for val in s:
        if val == "{":
            if flag == 0:
                flag = 1
                start = []
        elif val.isdigit():
            if flag == 1:
                now += val
        elif val == "}":
            if flag == 1:
                if now != '':
                    start.append(int(now))
                    now = ''
                answer.append((start,len(start)))
                flag = 0
        elif val == ',':
            if now != '':
                start.append(int(now))
                now = ''
    answer.sort(key = lambda x:x[1])    # 개수별 정렬
    final = []      # 최종 답 리스트
    # 없는 숫자 append
    for i in range(len(answer)):
        for val in answer[i][0]:
            if val not in final:
                final.append(val)
                break
    return final