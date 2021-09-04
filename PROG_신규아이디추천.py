def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    first = True
    
    for i in range(len(new_id)):
        if len(answer) > 0:
            first = False
        if new_id[i].islower() or new_id[i].isdigit():
            answer += new_id[i]
        elif new_id[i] == "-" or new_id[i] == "_":
            answer += new_id[i]
        elif new_id[i] == '.':
            if first == True:
                continue
            elif answer[-1] == '.':
                continue
            else:
                answer += new_id[i]
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip('.')
    if len(answer) == 0:
        answer += 'a'
    if len(answer) < 3:
        now = answer[-1]
        answer += (now *3)
        answer = answer[:3]
    
    
    return answer