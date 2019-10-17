import sys
from bcrypt import hashpw, gensalt
from datetime import datetime


class User(object):
    def __init__(self, username='No name', password=None):
        self.username = username
        self.password = hashpw(password.encode('utf-8'), gensalt())
        self.created = datetime.now()
        self.client_ip = None  # pull the client ip address
        self.remote_ip = None
        self.is_active = False

    def __repr__(self):
        pass

    def set_username(self, username):
        self.username = str(username)

    def get_username(self):
        return self.username

    def set_to_active(self):
        self.is_active = True

    def json(self):
        return {
            'username': self.get_username()
        }


class Network(object):
    def __init__(self, affinnity, interations, User):
        self.affinity = affinity
        self.interations = interactions
        self.relation = User
        self.network = []

    def set_interations(self, num):
        self.interations = num

    def get_interations(self):
        return self.interations

    def set_affinity(self, num):
        self.affinity = num

    def get_affinity(self):
        return self.affinity

   def add_to_network(self, User)



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


def test_json():
    # create new User()
    ben = User()
    # set a username to - 'ben'
    ben.set_username('ben')
    # create json object
    data = ben.json()
    # test dictionary
    test = {
        'username': 'ben'
    }
    # ensure json() returns key value pair of instance variables
    assert data == test
