if __name__ == '__main__':    
    list1, list2 = [int(x) for x in input().split()], [int(y) for y in input().split()]
    def removal(list1, list2):
        ans1 = len(list1.intersection(list2))
        ans2 = len(list1.symmetric_difference(list2))
        ans3 = len(list1 - list2)
        ans4 = len(list2 - list1)
        return [ans1, ans2, ans3, ans4]
    if __name__ == '__main__':
        print(removal(set(list1), set(list2)))