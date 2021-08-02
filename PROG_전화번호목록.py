def solution(phone_book):
    answer = True
    phone_book.sort()       # 오름차순 sorting
    tot = len(phone_book)
    # (tot-1)만큼 반복
    for i in range(tot-1):
        if len(phone_book[i+1]) > len(phone_book[i]):   # 다음 글자수가 현재 글자수보다 크면
            # 현재 글자수가 다음 글자수 앞에 포함되어 있으면 => break
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:   
                answer = False
                break
    return answer