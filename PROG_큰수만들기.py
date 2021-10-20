def solution(number, rem):
    answer = ''
    stack = []
    k = rem
    nums = list(map(int,number))
    # 전체 숫자 비교
    for num in nums:
        # 스택이 안 비었고, k>0이면
        while stack and k > 0:
            if num > stack[-1]: # num이 이전값보다 크면
                stack.pop()     # 이전값 빼고, k -= 1
                k -= 1
            else:               # 이전값이 크면 break
                break
        stack.append(num)
    # 숫자 개수 = 전체 숫자 - k 개
    answer = ''.join(map(str,stack[:len(nums)-rem]))
    return answer