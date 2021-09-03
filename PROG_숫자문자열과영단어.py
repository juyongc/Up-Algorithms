def solution(s):
    answer = ""
    tot = len(s)
    numbers = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
    }
    now = ''
    
    for i in range(tot):
        if s[i].isdigit():  # 숫자면 이전값들 딕셔너리에서 찾기
            if now in numbers.keys():
                answer += str(numbers[now])
                now = ''
            answer += s[i]
        else:               # 문자면 하나씩 더하면서 딕셔너리에서 찾기
            now += s[i]
            if now in numbers.keys():
                answer += str(numbers[now])
                now = ''
    return int(answer)