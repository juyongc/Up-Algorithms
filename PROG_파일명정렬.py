def solution(files):
    answer = []
    arr = []
    # 모든 파일 체크해서 Head / Number 파트 나누기
    for i in range(len(files)):
        file = files[i]
        now = [i,'',0]
        flag = 0
        num = ''
        for j in range(len(file)):
            if file[j].isdigit():   # 숫자면
                flag = 1            # 플래그 체크
                num += file[j]
            else:                   # 문자면
                if flag:            # 숫자 이미 체크한 상태면 => break
                    break
                else:               # 아니면 => Head에 추가
                    now[1] += file[j].lower()
        now[2] = int(num)           # 숫자 추가
        arr.append(now)
    arr.sort(key = lambda x: (x[1],x[2]))   # 문자/숫자 순으로 정렬
    for a in arr:
        answer.append(files[a[0]])
    return answer