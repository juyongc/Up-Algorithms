import sys

inputs = sys.stdin
cnt = 0     # 데이터 분류용
attend = set()  # 출석 명단, 체크용
checked = 0     # 최종 출석 확인
for datas in inputs:
    # 데이터 분류
    if cnt == 0:    # 처음 값은 시간값 종류
        S,E,Q = datas.split()
        cnt += 1
    else:
        time,name = datas.split()
        if S >= time:           # 개총 전 참석자 확인
            attend.add(name)    # 명단에 추가
        if E <= time <= Q:      # 개총 후 참석자 확인
            if name in attend:  # 이름이 있으면
                checked += 1    
                attend.remove(name) # 이름 제거
print(checked)