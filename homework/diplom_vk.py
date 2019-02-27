import asyncio
import aiohttp
import async_timeout
import requests
from pprint import pprint
# coding=utf-8
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
        groups_id = data['response']['items']
        id_list = []
        for group_id in groups_id:
            id_list.append(group_id['id'])
        return id_list

    # Получаю список id друзей
    def friends_list(self):
        params = self.get_params()
        params['fields'] = None
        params['count'] = 1
        request_url = 'https://api.vk.com/method/'
        api_method = 'friends.get'
        response = requests.get(f'{request_url}{api_method}', params, timeout=3).json()
        items = response['response']['items']
        friends_list = []
        return items

    # with async_timeout.timeout(0.001):
    #     def in_groups(self):
    #         group = self.groups()
    #         item = self.friends_list()
    #         params = {}
    #         params['v'] = '5.92'
    #         params['access_token'] = TOKEN
    #         params['user_ids'] = item
    #         total_list = {}
    #         for id in group:
    #             if id not in total_list.keys():
    #                 total_list[id] = list()
    #             params['group_id'] = id
    #             request_url = 'https://api.vk.com/method/'
    #             api_method = 'groups.isMember'
    #             response = requests.get(f'{request_url}{api_method}', params).json()
    #             # print(response)
    #             total_list[id].append(response)
    #         pprint(total_list)
    #         return total_list

    def in_groups(self):
        group = self.groups()
        item = self.friends_list()
        params = {}
        params['v'] = '5.92'
        params['access_token'] = TOKEN
        params['user_ids'] = item
        total_list = {}
        for id in group:
            if id not in total_list.keys():
                total_list[id] = list()
            params['group_id'] = id
            request_url = 'https://api.vk.com/method/'
            api_method = 'groups.isMember'
            response = requests.get(f'{request_url}{api_method}', params).json()
            total_list[id].append(response)
        pprint(total_list)
        return total_list


# Ожидаю получить словарь с ключём в виде id групп, а значение словарь со словарём jsom. Из получившегося большого словаря вытащить id групп , в которых нет друзей.
# Происходит ошибка 'error_code': 6.
# Извините за закоментированный код, но так я пробовал разобраться с таймаутом запросов.
if __name__ == '__main__':

    user1 = User(171691064)

    user1.groups()

    user1.friends_list()

    user1.in_groups()






















