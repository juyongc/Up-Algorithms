def solution(n,a,b):
    answer = 0

    while a != b:
        # 2로 나눈 몫이 같아지면 끝
        a,b = (a+1)//2, (b+1)//2
        answer += 1
        
    return answer