def solution(id_list, report, k):
    answer = [0]*len(id_list)
    id_dict = {}
    for i in range(len(id_list)):
        id_dict[id_list[i]] = i
    
    report = list(set(report))
    report_tot = {}
    for rep in report:
        reporter, reported = rep.split()
        if reported not in report_tot:
            report_tot[reported] = [reporter]
        else:
            report_tot[reported].append(reporter)
    
    for key,val in report_tot.items():
        if len(val) >= k:
            for v in val:
                answer[id_dict[v]] += 1
    
    return answer