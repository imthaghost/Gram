from instagram_private_api import Client, ClientCompatPatch
from getpass import getpass


user_name = 'foreignzeus'
password = getpass()

api = Client(user_name, password)
results = api.feed_timeline()
print(results)
