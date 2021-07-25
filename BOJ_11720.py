import sys

inputs = sys.stdin.readline
N = int(inputs())
nums = list(inputs().rstrip())  # 리스트에 분할해서 넣기
ans = 0
# 문자를 정수로 바꿔서 다 더하기
for num in nums:
    ans += int(num)
print(ans)