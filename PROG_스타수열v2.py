from collections import defaultdict
def solution(a):
    answer = 0
    
    if len(a) == 1:
        return 0
    
    a_dict = defaultdict(list)
    
    if a[0] != a[1]:
        a_dict[a[0]].append(1)
    # 인덱스의 전,후를 비교해서 이미 수열인지 아닌지 확인
    # 전,후가 같은 값이면 통과
    # 전이 다르면 => 현재 인덱스를 추가
    # 후만 다르면 => 인덱스 + 1 추가
    for i in range(1,len(a)):
        val = a[i]
        
        if i == len(a)-1:
            if a[i-1] != a[i]:
                if a_dict[val] and a_dict[val][-1] == i-1:
                    continue
                else:
                    a_dict[val].append(i) 
            continue
        # 전,후가 같으면 => 넘기기
        if a[i-1] == a[i] and a[i] == a[i+1]:
            continue
        # 전이랑 다르면
        if a[i-1] != a[i]:
            if a_dict[val] and a_dict[val][-1] == i-1:      # 이미 수열에 들어온 값인지 확인
                if a[i] != a[i+1]:                          # 후랑 비교
                    a_dict[val].append(i+1)
                continue
            else:
                a_dict[val].append(i)
        else:   # 전이랑 같으면 => 후는 다르니, 후값 추가
            a_dict[val].append(i+1)
    
    for key,val in a_dict.items():
        answer = max(answer,len(val)*2)
        
    return answer