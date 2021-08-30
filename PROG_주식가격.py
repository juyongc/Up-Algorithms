def solution(prices):
    answer = [0] * len(prices)  # 정답 리스트
    stack = []                  # 안떨어진 가격 인덱스
    stack.append(0)
    now = 1
    # 마지막 인덱스까지 비교
    while now < len(prices):
        cur = prices[now]       # 현재 가격
        # 모든 answer[스택값] += 1 
        for num in stack:
            answer[num] += 1
        # 스택 마지막값부터 비교
        # 떨어지면 pop / 아니면 break
        while stack:
            val = stack[-1]
            if prices[val] > cur:
                stack.pop()
            else:
                break
        stack.append(now)   # 현재 가격 인덱스 추가
        now += 1            # 다음 인덱스

    return answer