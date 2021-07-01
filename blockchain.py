import hashlib

chain = []  # 해시값 저장용
block = 0   # 블록 개수
nonce = 0   # 논스: 조건에 맞는 해시값의 정수값
data = 'Genesis Block'
prev = 'Start Genesis'  # 이전 해시값
# 현 논스에 대한 해시값
hashcode = hashlib.sha256(str(nonce).encode()).hexdigest()
chain.append(hashcode)

while block < 3:
    flag = 0    # 조건 확인용
    # Genesis Block 값
    if block == 0:
        data = 'Genesis Block'
        prev = 'Start'
        hashcode = hashlib.sha256(str(nonce).encode()).hexdigest()
        chain.append(hashcode)
        flag = 1
    # 그 후,
    else:
        hashcode = hashlib.sha256(str(nonce).encode()).hexdigest()
        cnt = 0
        # '0'이 연속으로 5번 나오는지 체크
        for i in range(5):
            if hashcode[i] == '0':
                cnt += 1
            else:
                break
        if cnt == 5:
            data = block
            prev = chain[block-1]
            chain.append(hashcode)
            flag = 1
    # 조건에 맞을 경우 -> 출력
    if flag == 1:
        print('nonce: {}\ndata: {}'.format(nonce,data))
        print('prevhash: {}\nhash: {}\n'.format(prev,hashcode))
        block += 1      # 블록 번호 ++

    nonce += 1          # 논스 ++
