import sys
from bcrypt import hashpw, gensalt

class User(object):
    def __init__(self):
        self.username = None

    def __repr__(self):
        pass
    
    def set_username(self, username):
        self.username = str(username)
    
    def get_username(self):
        return self.username


class Network(object):
    def __init__(self):
        pass

class assests(object):
    def __init__(self):
        pass

def test_set_username(username):
    # create new User()
    gary = User()
    # set username to argument
    gary.set_username(username)
    # ensure username value is not None
    assert gary.username 

def test_get_username():
    # create new User()
    kayvon = User()
    # set username to - 'kayvon'
    kayvon.set_username('kayvon')
    # ensure get_username() returns same value as instance variable username
    assert kayvon.get_username() == kayvon.username
   


