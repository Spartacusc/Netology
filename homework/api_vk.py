# Вам предстоит решить задачу поиска общих друзей у пользователей VK.
#
# Ссылка на документацию VK/dev.
#
# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сет


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
    # print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '7f1964d746efb6d5934bba9bcb5f865a68bf0c0ba6f3b4999fdc77397cd5a451f4a90e52bbd63d1f767bb'

class User:

    def __init__(self, id=None):
        self.id = id
        self.token = TOKEN

    # def __new__(cls,id):
    #     ID = id
    #     user = 'http:\VK.com\id' + str(ID)
    #     return user

    def get_params(self):
       return {
            'v': '5.92',
            'access_token': TOKEN,
            'source_uid': 70680070,
            'target_uid': self.id
        }

    def __and__(self, other):
        params = self.get_params()
        # print(params)
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        friends_dict = response.json()
        print('Количество общих друзей: ', len(friends_dict['response']))
        return friends_dict

user1 = User(61024852)

user2 = User(70680070)

user1 & user2

# print(user1)
# print(user2)