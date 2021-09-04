from itertools import combinations as combi

def solution(info, query):
    answer = [0]*len(query)
    infos = {}
    for val in info:
        now = val.split()
        for i in range(5):
            informs = list(map(''.join,combi(now[:4],i)))
            for inform in informs:
                if inform in infos:
                    infos[inform] += [int(now[-1])]
                else:
                    infos[inform] = [int(now[-1])]
    for val in infos:
        infos[val].sort()
    
    nquery = []
    cnt = 0
    
    for quer in query:
        nquer = quer.replace('and', ' ')
        nquer = nquer.replace('-', ' ')
        nquery = nquer.split()
        words = ''.join(nquery[:-1])
        wish = int(nquery[-1])
        if words in infos:
            scores = infos[words]
            if len(scores) == 1:
                if scores[0] >= wish:
                    answer[cnt] = 1
            else:
                s = 0
                e = len(scores)
                while s < e:
                    mid = (s+e)//2
                    if scores[mid] >= wish:
                        e = mid
                    else:
                        s = mid + 1
                now = e
                answer[cnt] = len(scores) - now
        cnt += 1

    return answer