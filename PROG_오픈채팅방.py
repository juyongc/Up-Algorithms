def solution(record):
    answer = []
    conditions = []
    nick = dict()
    for reco in record:
        cond = list(reco.split())
        conditions.append(cond)
    for condition in conditions:
        if condition[0] != 'Leave':
            nick[condition[1]] = condition[2]
    change = []
    for condition in conditions:
        if condition[0] == "Enter":
            change.append('{0}님이 들어왔습니다.'.format(nick[condition[1]]))
        elif condition[0] == "Leave":
            change.append('{0}님이 나갔습니다.'.format(nick[condition[1]]))
    
    return change