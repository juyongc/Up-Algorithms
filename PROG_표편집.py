# 링크드 리스트 & 딕셔너리
def solution(n, k, cmd):
    answer = ''
    linked_list = {i : [i-1,i+1] for i in range(n)}
    linked_list[0][0] = 0
    linked_list[n-1][1] = n-1
    recent = []
    check = ["O" for _ in range(n)]
    now = k
    # 명령어별 구현
    for cm in cmd:
        if cm[0] == "U":
            x,num = cm.split()
            num = int(num)
            for i in range(num):
                now = linked_list[now][0]
        elif cm[0] == "D":
            x,num = cm.split()
            num = int(num)
            for i in range(num):
                now = linked_list[now][1]
        # 삭제 후 행 변경
        elif cm[0] == "C":
            check[now] = "X"
            recent.append(now)
            down,up = linked_list[now]
            # 상황별 구현 => 첫 행 / 중간 / 마지막 행 
            if down == now:
                linked_list[up][0] = up
            elif up == now:
                linked_list[down][1] = down
            else:
                linked_list[down][1] = up
                linked_list[up][0] = down
            # 마지막 행이면 바로 윗 행 선택
            if up == now:
                now = down
            else:
                now = up
        # 행 복구
        else:
            recover = recent.pop()
            check[recover] = "O"
            down,up = linked_list[recover]
            # 상황별 구현 => 첫 행 / 중간 / 마지막 행 
            if down == recover:
                linked_list[up][0] = recover 
            elif up == recover:
                linked_list[down][1] = recover 
            else:
                linked_list[down][1] = recover 
                linked_list[up][0] = recover 
            
    answer = "".join(check)
    return answer