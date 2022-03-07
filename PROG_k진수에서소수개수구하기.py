# 소수 찾기 함수
def check_prime(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    # 제곱근까지만 확인
    for i in range(2,int(num**(1/2))+2):
        if num % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    binary = ""
    # 진수변환 => 몫이 0이 될때까지 나누기
    while n > 0:
        n,rem = divmod(n,k)
        binary += str(rem)
    binary = binary[::-1] + "0" # 마지막값도 계산할 수 있게 "0" 추가
    
    prime = ""
    for i in range(len(binary)):
        if binary[i] == "0":
            if prime:
                answer += check_prime(int(prime))
                prime = ""
        else:
            prime += binary[i]   
    return answer