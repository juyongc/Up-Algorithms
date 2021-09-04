from itertools import combinations as combi

def solution(orders, nums):
    answer = []
    arr = [[] for _ in range(len(nums))]
    course = {}
    for order in orders:
        cnt = len(order)
        tot = []
        order = ''.join(sorted(list(order)))
        for i in range(2,cnt+1):
            tot += list(map(''.join,combi(order,i)))
        # 조합 구하기 및 개수 카운팅
        for now in tot:
            if now in course:
                course[now] += 1
            else:
                course[now] = 1
                
    for key,value in course.items():
        if len(key) in nums and value > 1:
            now = nums.index(len(key))
            arr[now].append((key,value))
    for menus in arr:
        menus.sort(key = lambda x: x[1])
        if len(menus) > 0:
            maxi = menus[-1][1]
            for menu in menus:
                if menu[1] == maxi:
                    answer.append(menu[0])
    answer.sort()
    return answer