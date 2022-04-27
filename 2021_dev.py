def solution(lottos, win_nums):
    # IndexError: list index out of range 오류 발생으로 맞추기 위함
    rank = [6,6,5,4,3,2,1]
    #찾고자하는 항목이 파이썬 리스트에 몇개나 들어잇는지 확인 - count
    cont = lottos.count(0)
    ans = 0
    #if A in B :B안에 A가 있으면 참이다 
    #if A not in B :B안에 A가 없으면 참이다 
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cont+ans], rank[ans]