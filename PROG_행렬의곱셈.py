def solution(array1, array2):
    answer = []
    # array1 모든 행 반복
    for arr1 in array1:
        narr = [0]*len(array2[0])
        # array2 열 수 X arr1 해당 행 
        for i in range(len(array2[0])):
            for j in range(len(arr1)):
                narr[i] += arr1[j]*array2[j][i]
        answer.append(narr)
    return answer