import hashlib
from utils.testtools import test_fixture


class PwdDB(object):
    def __init__(self) -> None:
        super().__init__()
        self._db = {}

    def set_user(self, user:str, pwd:str) -> None:
        value = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        if user in self._db and self._db[user] != value:
            print(f'Update password for {user}.')
        else:
            print(f'Set password for {user}')        
        self._db[user] = value

    def check_pwd(self, user:str, pwd:str) -> bool:
        value = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        if user not in self._db:
            return False
        return self._db[user] == value


def test_pwddb():
    users = {
        'Bob':'1234',
        'John':'big_joke@me',
        'Stephanie':'you guess',
    }
    pwdDb = PwdDB()
    pwdDb.set_user('Bob','0000')
    for k,v in users.items():
        pwdDb.set_user(k, v)
    data = {
        (('Bob', '1234',), True),
        (('John', 'big_joke@me'), True),
        (('Stephanie', 'you guess',), True),
        (('NoName', 'Invalid pass'), False),
        (('Bob', 'Wrong password'), False),
    }
    test_fixture(pwdDb.check_pwd, data)



def test():
    test_pwddb()


test()
