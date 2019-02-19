# Есть вещи, которые объединяют людей, а есть те, которые делают нас индивидуальными. Давайте посмотрим, чем пользователи в ВК не делятся со своими друзьями?
#
# Задание:
# Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей. В качестве жертвы, на ком тестировать, можно использовать: https://vk.com/eshmargunov
#
# Входные данные:
# Имя пользователя или его id в ВК, для которого мы проводим исследование.
#
# Внимание: и имя пользователя (eshmargunov) и id (171691064) - являются валидными входными данными.
#
# Ввод можно организовать любым способом:
#
# из консоли
# из параметров командной строки при запуске
# из переменной
# Выходные данные:
# Файл groups.json в формате:
#
# [
#     {
#     “name”: “Название группы”,
#     “gid”: “идентификатор группы”,
#     “members_count”: количество_участников_сообщества
#     },
#     {
#     …
#     }
# ]
# Форматирование не важно, важно чтобы файл был в формате json
#
import requests
from pprint import pprint

TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.token = TOKEN

    def get_params(self):
        return {
            'v': '5.92',
            'access_token': TOKEN,
            'user_id': self.user_id,
            'extended': 1,
            'fields': ['name', 'id', 'members_count'],
            'count': 1
        }

    def groups(self):
        params = self.get_params()
        request_url = 'https://api.vk.com/method/'
        api_method = 'groups.get'
        data = requests.get(f'{request_url}{api_method}', params).json()
        pprint(data)

    def friends_list(self):
        params = self.get_params()
        params['fields'] = None
        request_url = 'https://api.vk.com/method/'
        api_method = 'friends.get'
        response = requests.get(f'{request_url}{api_method}', params).json()
        items = response['response']['items']
        friends_list = []
        for friends in items:
            friend = User(friends)
            friends_list.append(friend)
        # pprint(friends_list)
        return friends_list

if __name__ == '__main__':

    user1 = User(171691064)

    # user1.groups()

    user1.friends_list()

    for item in user1.friends_list():
        # pprint(item)
        pprint(item.groups())





















