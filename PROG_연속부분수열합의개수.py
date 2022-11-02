def solution(elements):
    answer = 0
    # 마지막 원소도 이전 원소값까지 알 수 있도록 늘려주기
    circular = elements[:] + elements[:len(elements)-1]
    
    answer_set = set()
    answer_list = [0]*len(elements)
    # 기존 엘리먼트 합에 다음 엘리먼트 더해서
    # 길이를 늘리며 부분 수열 합 키우기
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer_list[j] += circular[i+j]
        for ans in answer_list:
            answer_set.add(ans)
            
    answer = len(answer_set)
    return answer