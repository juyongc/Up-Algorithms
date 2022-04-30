def binary(num):
    
    conv = ''
    zero = -1
    cnt = 0
    # 2진수 변환
    while num > 0:
        num,rem = divmod(num,2)
        # 가장 처음에 나오는 '0' 찾기
        if rem == 0 and zero == -1:
            zero = cnt
        cnt += 1
        conv += str(rem)
        
    return conv[::-1],zero


def solution(numbers):
    answer = []
    
    for num in numbers:
        if num == 0:
            answer.append(1)
            continue
        res,flag = binary(num)
        bit = num
        if flag == -1:      # 111 => 1011 (앞에 +1, 바로 뒤 = 0)
            bit += (2 ** len(res) - 2**(len(res)-1))
        else:               # 101 => 110 (첫 0 => 1, 바로 뒤 = 0)
            bit += 2 ** flag
            if flag != 0:
                bit -= 2 ** (flag-1)
        answer.append(bit)
    return answer