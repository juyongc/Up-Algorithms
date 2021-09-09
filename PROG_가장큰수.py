def solution(numbers):
    answer = ''
    nums = [(str(number)*3)[:4] for number in numbers]  # 4자리까지 올리기
    nnums = []
    # 추후 인덱스 확인할 수 있게 튜플만들기
    for idx,num in enumerate(nums):
        nnums.append((idx,num))
    nnums.sort(key= lambda x: x[1], reverse=True)   # 정렬
    for nnum in nnums:
        answer += str(numbers[nnum[0]])
    answer = str(int(answer))
    return answer