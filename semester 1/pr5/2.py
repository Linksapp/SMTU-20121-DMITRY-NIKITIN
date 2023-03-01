from itertools import combinations
if __name__ == '__main__': 
    list1 = [int(x) for x in input().split()]
    list2 = set()
    for num in range(1, len(list1)+1):
        x = combinations(list1, num)
        for y in x:
            list2.add(y)
    print(list2)







