import sys

inputs = sys.stdin
for line in inputs:
    if line.rstrip() == "END":      # 문자열이 == "END"면 끝
        break
    else:                           # 아니면 역으로 출력
        print(line.rstrip()[::-1])