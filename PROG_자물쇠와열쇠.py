# 0,90,180,270 회전 함수
def make_key(sample,num):
    n = len(sample)
    key = [[0]*n for _ in range(n)]
    if num == 0:        # 0도
        return sample
    elif num == 1:      # 90도
        for i in range(n):
            for j in range(n):
                key[i][j] = sample[j][n-i-1]
        return key
    elif num == 2:      # 180도
        for i in range(n):
            for j in range(n):
                key[i][j] = sample[n-i-1][n-j-1]
        return key
    else:               # 270도
        for i in range(n):
            for j in range(n):
                key[i][j] = sample[n-j-1][i]
        return key
            

def solution(key, lock):
    answer = True
    sample_key = key[:]
    krow,kcol = len(key),len(key[0])
    lrow,lcol = len(lock),len(lock[0])
    
    # lock 행,열 앞,뒤로 (key-1)개씩 빈 칸 추가
    con_lock = [[0]*(2*(kcol-1)+lcol) for _ in range(2*(krow-1)+lrow)]
    for i in range(krow,krow+lrow):
        for j in range(kcol,kcol+lcol):
            con_lock[i-1][j-1] = lock[i-krow][j-kcol]
                
    for i in range(krow,krow+lrow):
        for j in range(kcol,kcol+lcol):
            con_lock[i-1][j-1] = lock[i-krow][j-kcol]
    
    # 4방향으로 키 만들고, 한 칸씩 움직이면서 자물쇠와 키 확인하기
    for i in range(4):
        key_now = make_key(sample_key,i)        # 회전한 키 만들기
        for r in range(krow+lrow-1):
            for c in range(kcol+lcol-1):
                # 현재 키 위치 자물쇠 위치에 더하기
                for x in range(krow):
                    for y in range(kcol):
                        if key_now[x][y] == 1:
                            con_lock[r+x][c+y] += 1
                flag = 0
                # 자물쇠 부분 모두 1인지 확인
                for lx in range(lrow):
                    for ly in range(lcol):
                        if con_lock[krow+lx-1][kcol+ly-1] != 1:
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 0:
                    return True
                # 자물쇠 복구하기
                for x in range(krow):
                    for y in range(kcol):
                        if key_now[x][y] == 1:
                            con_lock[r+x][c+y] -= 1
                
    return False