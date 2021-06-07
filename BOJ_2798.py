import sys

def blackjack(n,m):
    maxi = 0
    # 카드 세장 뽑기
    # a < b < c
    for a in range(n-2):
        if cards[a] >= m:
            break
        for b in range(a+1,n-1):
            if cards[a]+cards[b] >= m:
                break
            for c in range(b+1,n):
                hit = cards[a] + cards[b] + cards[c]
                if hit > m:
                    break
                elif hit == m:
                    maxi = hit
                    return maxi
                else:
                    if hit > maxi:
                        maxi = hit
    return maxi


inputs = sys.stdin.readline

N,M = map(int,inputs().split())
cards = list(map(int,inputs().split()))
cards.sort()        # 숫자 크기별 정렬
ans = blackjack(N,M)

print(ans)