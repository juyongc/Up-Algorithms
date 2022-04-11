import sys
inputs = sys.stdin.readline


def find_word(s1,word):
    if len(word) > len(s1):
        return "FRULA"

    stack = []
    for w in s1:
        stack.append(w)
        # word의 마지막 단어랑 같으면 비교
        if w == word[-1]:
            now = "".join(stack[-len(word):])
            if now == word:
                for _ in range(len(word)):
                    stack.pop()
    now = "".join(stack)
    if now == "":
        return "FRULA"
    else:
        return now


s1 = input()
word = input()
answer = find_word(s1,word)
print(answer)