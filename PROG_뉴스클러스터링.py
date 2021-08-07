def solution(str1, str2):
    answer = 0

    dic1, dic2 = dict(), dict()
    # str1,str2 2단어씩 끊어서
    # 알파벳이면 소문자 변형해서 dic에 넣기
    for i in range(len(str1) - 1):
        word = str1[i:i + 2]
        if word.isalpha():
            word = word.lower()
            if word not in dic1:
                dic1[word] = 1
            else:
                dic1[word] += 1
    for i in range(len(str2) - 1):
        word = str2[i:i + 2]
        if word.isalpha():
            word = word.lower()
            if word not in dic2:
                dic2[word] = 1
            else:
                dic2[word] += 1

    same = 0    # 교집합 문자 개수
    # dic1에 dic2랑 같은 문자 same에 더하기
    for key in dic2.keys():
        if key in dic1:
            same += min(dic2[key], dic1[key])
    tot = 0     # 합집합 문자 개수
    # 합집합 = 전체 개수 - 교집합 개수
    for val in dic1.values():
        tot += val
    for val in dic2.values():
        tot += val
    tot -= same
    # 조건에 따른 출력
    if tot == 0:
        answer = 65536
    else:
        answer = int((same / tot) * 65536)

    return answer