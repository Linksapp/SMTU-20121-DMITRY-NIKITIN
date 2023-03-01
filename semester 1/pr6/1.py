def santa_users(users_list):
    santa_list = {}
    for user in users_list:
        if len(user) == 1:  
            user_dict = {user[0] : None}
        else:
            user_dict = {user[0] : user[1]}
        santa_list.update(user_dict)
    return santa_list
if __name__ == '__main__': 
    example_list = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
    print(santa_users(example_list))