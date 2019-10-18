import sys
from bcrypt import hashpw, gensalt
from datetime import datetime


class User(object):
    def __init__(self, username='No name'):
        self.username = username
        self.full_name = None
        self.created = datetime.now()
        self.client_ip = None  # pull the client ip address
        self.remote_ip = None
        self.is_active = False
        self.followers = None
        self.follower_count = None
        self.following_count = None
        self.id = None
        self.rank_token = None
        self.network = None
        self.picture = None
        self.likes = []

    def __repr__(self):
        pass

    def set_follower_count(self, num):
        self.follower_count = int(num)

    def get_follower_count(self):
        return self.follower_count

    def set_following_count(self, num):
        self.following_count = int(num)

    def get_following_count(self):
        return self.following_count

    def set_username(self, username):
        self.username = str(username)

    def get_username(self):
        return self.username

    def set_to_active(self):
        self.is_active = True

    def set_name(self, name):
        self.full_name = str(name)

    def get_full_name(self):
        return self.full_name

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_rank_token(self, token):
        self.rank_token = token

    def get_rank_token(self):
        return self.rank_token

    def set_network(self, arr):
        self.network = Network(arr)

    def set_likes(self, item):
        self.likes.append(item)

    def set_picture(self, src):
        self.picture = str(src)

    def get_picture(self):
        return self.picture

    def get_likes(self):
        return self.likes

    def json(self):
        return {
            'username': self.get_username(),
            'is_active': self.is_active,
            'follower_count': self.follower_count,
            'following_count': self.following_count,
            'profile_picture': self.picture,
            'full_name': self.full_name
            # 'likes': self.get_likes()
        }


class Network(object):
    def __init__(self, network):
        self.affinity = None
        self.interations = None
        self.network = network
        self.username = []
        self.fullname = []

    def set_interations(self, num):
        self.interations = num

    def get_interations(self):
        return self.interations

    def set_affinity(self, num):
        self.affinity = num

    def get_affinity(self):
        return self.affinity

    def add_to_network(self, User):
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
