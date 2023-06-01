class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email


class Catalog:
    def __init__(self, data: list[tuple[str, str, int]]):
        self.data = data
        self.user_catalog = {}

    @staticmethod
    def _email_check(mail):
        if '@' in mail and len(mail[:mail.find('@')]) > 1 and len(mail[mail.find('@'):]) > 1 and '.' in mail[mail.find('@'):]:
            return 1
        else: return 0

    def checker(self):
        for user in self.data:
            try:
                assert not(user[0] in self.user_catalog), "This username is already taken"
                assert user[2] >= 16, "You have to be over 16"
                assert Catalog._email_check(user[1]), "Such email adress doesn't exist"
                self.user_catalog[f'{user[0]}'] = User(user[0], user[1])
            except AssertionError as error:
                print(error)
                continue

test_users = [('Joe', 'myemail@gmail.com', 19), ('Bob', 'm@gmail', 25), ('John', 'john2010@gmail.com', 13), ('Joe', 'jo_e@gmail.com', 23)]
    
example = Catalog(test_users)
example.checker()
print(example.user_catalog)
