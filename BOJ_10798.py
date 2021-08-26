import sys

words = ['']*15
for _ in range(5):
    inputs = sys.stdin.readline
    letters = inputs().rstrip()
    # 글자 하나씩 리스트 해당 인덱스 ++ 
    for i in range(len(letters)):
        words[i] += letters[i]
ans = ''.join(words)    # 전부 합치기
print(ans)
