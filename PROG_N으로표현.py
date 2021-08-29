# N을 1부터 1씩 올리면서 답 체크
# (N-1 <-> 1 / N-2 <-> 2 / ... / N-i <=> i) 식으로 
# 계산해야 해서 dp로 품
def solution(N, number):
    answer = -1

    if N == number:
        answer = 1
    else:
        now = 2
        curs = [list() for _ in range(9)]
        curs[1].append(N)
        # 8보다 크면, 답 = -1
        while now <= 8:
            tot = now // 2
            nplus = int(str(N) * now)
            # nplus가 정답인지 확인
            if nplus == number:
                answer = now
                return answer
            else:
                curs[now].append(int(str(N) * now))    
            # (tot -i <=> i) 값끼리 계산해서 답 있는지 확인 
            for i in range(1, tot + 1):
                for num in curs[now - i]:
                    for val in curs[i]:
                        plus = val + num
                        minus = val - num
                        minus2 = num - val
                        multi = val * num
                        this = [plus, minus, minus2, multi]
                        if num != 0:
                            divid = val // num
                            this.append(divid)
                        if val != 0:
                            divid2 = num // val
                            this.append(divid2)
                        if number in this:
                            answer = now
                            return answer
                        else:
                            curs[now] += this
            curs[now] = list(set(curs[now]))
            now += 1

    return answer