def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        stand = scores[i][i]
        now = []
        maxi,mini = 0,0
        # 각 열별 유일한 최고점/최저점 여부 확인
        for j in range(len(scores)):
            if i != j:
                if scores[j][i] > stand:
                    maxi = 1
                elif scores[j][i] == stand:
                    maxi = 1
                    mini = 1
                else:
                    mini = 1
                now.append(scores[j][i])
        if maxi == 1 and mini == 1: # 아니면 자신 점수도 append
            now.append(stand)
        # 학점 정하기
        tot = sum(now) // len(now)
        if tot >= 90:
            answer += 'A'
        elif 80<= tot < 90:
            answer += 'B'
        elif 70<= tot < 80:
            answer += 'C'
        elif 50<= tot < 70:
            answer += 'D'
        else:
            answer += 'F'
        
    return answer