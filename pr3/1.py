from itertools import permutations as permut

if __name__ == '__main__':
    N = int(input())
    input_numbers = [int(input()) for _ in range(N)]
    C = int(input())
    goal_list = []
    goal_sum = 10**10
    members = list(permut(input_numbers, 4))
    for uniq in members:
        if C == 0:
            if abs(sum(uniq)) < goal_sum:
                goal_list = uniq
                goal_sum = sum(uniq)
        if abs(C - sum(uniq)) < goal_sum:
            goal_sum = abs(C - sum(uniq))
            goal_list = uniq
    print(list(goal_list))
    print(sum(goal_list))