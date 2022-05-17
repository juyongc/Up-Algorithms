def solution(id_list, report, k):
    answer = [0]*len(id_list)
    id_dict = {}
    # 유저 순서 딕셔너리화
    for i in range(len(id_list)):
        id_dict[id_list[i]] = i
    
    reported = {}
    # {신고된 유저 : set(신고한 유저)} 딕셔너리화
    for rep in report:
        reporter,user = rep.split(" ")
        if user not in reported:
            reported[user] = {reporter}
        else:
            reported[user].add(reporter)
    # k번 이상 신고된 유저 찾기 & 신고한 유저 카운팅해주기
    for key,val in reported.items():
        if len(val) < k:
            continue
        reporter_list = list(val)
        for name in reporter_list:
            answer[id_dict[name]] += 1
    
    return answer