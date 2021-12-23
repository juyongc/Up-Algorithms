def solution(expression):
    answer = 0
    nums = []       # 숫자 저장용
    opers = []      # 연산자 저장용
    num = ''
    # 숫자와 연산자 구분하기
    for express in expression:
        if express.isdigit():
            num += express
        else:
            opers.append(express)
            nums.append(int(num))   # int로 변환 후 추가
            num = ''
    nums.append(int(num))
    
    combis = ["+-*","+*-","*+-","*-+","-+*","-*+"]  # 가능한 모든 연산자 조합

    for i in range(6):          # 가능한 조합 => 6번 
        combi = combis[i]       # 현재 연산자 조합
        numbers = nums[:]       # 수 리스트
        operands = opers[:]     # 연산자 리스트
        
        for k in range(3):
            ntemp = []          # 계산 후 수 리스트
            otemp = []          # 계산 후 연산자 리스트
            ntemp.append(numbers[0])    # 첫번째 값 자동 추가
            rot = len(operands)
            for j in range(rot):
                operand = operands[j]
                if operand == combi[k]: # 현재 연산자가 우선순위 연산자라면
                    now = ntemp.pop()   # 계산 후 리스트에서 마지막 값 꺼내오기
                    # 연산자별 연산
                    if operand == "+":
                        ntemp.append(now + numbers[j+1])
                    elif operand == "-":
                        ntemp.append(now - numbers[j+1])
                    else:
                        ntemp.append(now * numbers[j+1])
                else:                   # 아니면 => 연산자 / 다음 수 추가
                    otemp.append(operand)
                    ntemp.append(numbers[j+1])
            # 연산자 / 숫자 갱신
            numbers = ntemp[:]
            operands = otemp[:]
        answer = max(answer,abs(numbers[0]))    # max값 계산
    return answer