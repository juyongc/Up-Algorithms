# 10진수로 변환
def convert(num,jinsu):
    global number
    now = ""
    while num > 0:
        num,rem = divmod(num,jinsu)
        now += number[rem]
    now = now[::-1]
    return now

def solution(n, t, m, p):
    global number
    answer = ''
    number = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",
              10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    total = "0"
    cnt = 0
    max_num = t*m + p               # 최대 사이즈
    # n진수로 변환한 문자열 합한 개수가 최대 사이즈보다 커지면 stop
    while len(total) < max_num:
        total += convert(cnt,n)
        cnt += 1
    for i in range(t):
        answer += total[p-1+m*i]    # p-1 => 0부터 시작할 수 있게
    return answer