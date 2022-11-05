from collections import deque
def solution(order):
    answer = 0
    sub_belt = []
    belt = deque(i for i in range(1,len(order)+1))
    
    for num in order:
        if belt and num >= belt[0]:
            while belt:
                if num > belt[0]:           # 필요한 상자가 벨트에 있다면 => 현재 상자 보조 벨트에 추가
                    sub_belt.append(belt.popleft())
                elif num == belt[0]:        # 필요한 상자 찾았으면 => 정답 갱신
                    belt.popleft()
                    answer += 1
                    break
        else:                               # 필요한 상자가 보조 벨트에 있다면
            if sub_belt and sub_belt[-1] == num:    # 보조 벨트의 마지막이면 => 꺼내기
                sub_belt.pop()
                answer += 1
            else:                                   # 마지막 아니면 => 불가
                break
            
    return answer