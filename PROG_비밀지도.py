def solution(n, arr1, arr2):
    num1 = max(arr1)
    num2 = max(arr2)
    maxi = max(num1,num2)
    cnt = 0
    flag = 0
    ## 최대 숫자의 비트 수 찾기
    while maxi > 1:
        if maxi%2 != 0:
            flag = 1
        maxi = maxi//2
        cnt += 1
    cnt += flag
    narr1 = []      # 두 지도 합쳐질 리스트
    # 첫번째 지도 (1 -> '#' / 0 -> ' ')
    for num in arr1:
        now = num
        conv = [" "]*cnt
        for i in range(cnt):
            bi = 2 ** (cnt-i-1)
            if now >= bi:
                now -= bi
                conv[i] = "#"
        narr1.append(conv)
    # 두번째 지도 (1 -> '#' / 0 -> ' ')
    for j in range(len(arr2)):
        now = arr2[j]
        for i in range(cnt):
            bi = 2 ** (cnt-i-1)
            if now >= bi:
                now -= bi
                narr1[j][i] = "#"
    final = []  # 일차원으로 정리한 지도
    for i in range(len(narr1)):
        final.append("".join(narr1[i]))

    return final