# doesn't work 
if __name__ == '__main__':
    N = int(input())
    input_numbers = [int(input()) for x in range(N)]
    C = int(input())
    goal_list = []
    while input_numbers:
        if C > 0:
            if min(input_numbers) > C and min(input_numbers) > 0:
                goal_list.append(min(input_numbers))
                input_numbers.remove(min(input_numbers))
            # goal_list.append(max(input_numbers))
            # input_numbers.remove(max(input_numbers))
            # if sum(goal_list) > 
            else: input_numbers.remove(min(input_numbers))