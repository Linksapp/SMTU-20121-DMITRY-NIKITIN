def candy_packages(cand, pack):
    if cand == pack:
        return 1
    elif pack == 0 or cand == 0 or pack > cand:
        return 0
    else:
        return candy_packages(cand-1, pack-1) + pack * candy_packages(cand-1, pack)

if __name__ == '__main__':    
    candies = int(input())
    packages = int(input())
    if not candy_packages(candies, packages):
        print('no solution')
    else: print(candy_packages(candies, packages))