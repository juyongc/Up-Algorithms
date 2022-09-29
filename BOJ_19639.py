import sys
inputs = sys.stdin.readline

X,Y,M = map(int,inputs().split())

enemy, medic = [],[]
for i in range(X):
    enemy.append((int(input()),i))
for i in range(Y):
    medic.append((int(input()),i))
enemy.sort()
medic.sort()

idx_e,idx_m = 0,0   # 현재 적, 현재 약 인덱스
orders = []         # 적,약 순서대로 저장
die = 0

hp = M
# 죽일 적이 남았거나 먹을 약이 남았으면 반복
while idx_e < len(enemy) or idx_m < len(medic):
    # 다 죽였으니 남은 약 다 먹기
    if idx_e >= len(enemy):
        orders.append(medic[idx_m][1]+1)
        idx_m += 1
        continue
    # 약 다 먹었으니 남은 적 죽일 수 있으면 죽이기
    if idx_m >= len(medic):
        hp -= enemy[idx_e][0]
        if hp <= 0:
            die = 1
            break
        orders.append(-(enemy[idx_e][1]+1))
        idx_e += 1
        continue
    
    # hp가 다음 적한테 맞아도 많으면 => 적 죽임
    # 아니면 => 약 먹음
    if hp > enemy[idx_e][0]:
        hp -= enemy[idx_e][0]
        orders.append(-(enemy[idx_e][1]+1))
        idx_e += 1
    else:
        hp += medic[idx_m][0]
        orders.append(medic[idx_m][1]+1)
        if hp >= M:     # 최대 체력 제한
            hp = M
        idx_m += 1

# 상황에 따른 출력
if die:
    print(0)
else:
    for o in orders:
        print(o)
