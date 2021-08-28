def solution(food_times, k):
    answer = 0
    eats = food_times[:]
    tot = sum(eats)
    if k >= tot:
        answer = -1
    else:
        num = len(eats)
        i = 0
        while k >= 0:
            i = i % num
            if eats[i] > 0:
                eats[i] -= 1
                if k == 0 :
                    answer = (i%num)+1
                    break
                else:
                    k -= 1
            i += 1
    return answer