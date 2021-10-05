def solution(word):
    answer = 0
    alpha = {'A':0,'E':1,'I':2,'O':3,'U':4}
    for i in range(len(word)):
        if word[i] == 'A':
            answer += 1
        else:
            now = alpha[word[i]]
            for j in range(4,i,-1):
                answer += now*(5**(j-i))
            answer += now + 1
    return answer