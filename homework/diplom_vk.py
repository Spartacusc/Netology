
import requests
from pprint import pprint

TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.token = TOKEN

    # Общие параметры к методам это нормально? Или для каждого метода отдельно писать?
    def get_params(self):
        return {
            'v': '5.92',
            'access_token': TOKEN,
            'user_id': self.user_id,
            'extended': 1,
            'fields': ['name', 'id', 'members_count'],
            'count': 1000
        }

    # Получаю список id  групп
    def groups(self):
        params = self.get_params()
        request_url = 'https://api.vk.com/method/'
        api_method = 'groups.get'
        data = requests.get(f'{request_url}{api_method}', params).json()
        # pprint(data)
        groups_id = data['response']['items']
        # pprint(groups_id)
        id_list = []
        for group_id in groups_id:
            # pprint(group_id['id'])
            id_list.append(group_id['id'])
        # pprint(id_list)
        return id_list

    # Получаю список id друзей
    def friends_list(self):
        params = self.get_params()
        params['fields'] = None
        params['count'] = None
        request_url = 'https://api.vk.com/method/'
        api_method = 'friends.get'
        response = requests.get(f'{request_url}{api_method}', params).json()
        items = response['response']['items']
        friends_list = []
        # pprint(items)
        # for friends in items:
        #     friend = User(friends)
        #     friends_list.append(friend)
        # pprint(friends_list)
        return items

    # Пробую получить информацию о том является ли каждый друг участником каждой группы
    def in_groups(self):
        group = groups()
        item = friends_list()
        params = self.get_params()
        params['user_ids'] = item
        params['fields'] = None
        params['count'] = None
        total_list = []
        for id in group:
            params['group_id'] = id
            request_url = 'https://api.vk.com/method/'
            api_method = 'groups.isMember'
            response = requests.get(f'{request_url}{api_method}', params).json()
            total_list.append(response)
        # pprint(total_list)
        return total_list

# Не получается присвоить функции groups() и friends_list() внутри функции in_groups.
# Ожидаю получить список со словарем, где ключ id групп ,а значение кол-во друзей в группах.

if __name__ == '__main__':

    user1 = User(171691064)

    user1.groups()

    user1.friends_list()

    user1.in_groups()

    # for item in user1.friends_list():
    #     # pprint(item)
    #     pprint(item.in_groups())





















