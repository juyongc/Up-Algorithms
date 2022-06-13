import sys
inputs = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        N = int(input())
        lego = [int(input()) for _ in range(N)]
        lego.sort()

        s,e = 0,N-1
        ans = [0,0]
        while s < e:
            se_sum = lego[s] + lego[e]

            if se_sum == x:
                ans = [lego[s],lego[e]]
                break
            elif se_sum > x:
                e -= 1
            else:
                s += 1

        if ans[0] == 0 and ans[1] == 0:
            print("danger")
        else:
            print("yes {} {}".format(ans[0],ans[1]))
    except:
        break