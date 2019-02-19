
from urllib.parse import urlencode
import requests
from pprint import pprint

def get_token():
    APP_ID = 6862050
    AUTH_URL = 'https://oauth.vk.com/authorize'
    auth_data = {
        'client_id': APP_ID,
        'scope': 'friends',
        'response_type': 'token',
        'v': '5.92'
    }
    print('?'.join((AUTH_URL, urlencode(auth_data))))

# get_token()

TOKEN = '7795c07dc6f1bef3bb4ee4a3735153645d4f18e0636791d1cdc7917030abef4b4be3b283ec60d5759ced9'

class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.token = TOKEN

    def __str__(self):
        user = 'http:\VK.com\id'
        return user + str(self.user_id)

    def get_params(self):
       return {
            'v': '5.92',
            'access_token': TOKEN,
            'source_uid': None,
            'target_uid': self.user_id
        }

    def __and__(self, other):
        params = self.get_params()
        params['source_uid'] = self.user_id
        params['target_uid'] = other.user_id
        request_url = 'https://api.vk.com/method/'
        api_method = 'friends.getMutual'
        data = requests.get(f'{request_url}{api_method}', params).json()
        # pprint(data)
        friends_list = []
        for friends in data['response']:
            friend = User(friends)
            friends_list.append(friend)
            # print(friend)
        pprint(friends_list)
        print('Количество общих друзей: ', len(data['response']))


user1 = User(70680070)

user2 = User(61024852)

user1 & user2

print(user1)
print(user2)