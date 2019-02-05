
from pprint import pprint

def get_cook_book():
    with open('Cook_book.txt') as f:
        cook_book = {}
        for line in f:
            keys = line
            # print(keys.strip())
            number = int(f.readline())
            while number != 0:
                value = f.readline().strip().split('|')
                number -= 1
                # print(value)
                if keys.strip() not in cook_book.keys():
                    cook_book[keys.strip()] = list()
                dishes = dict()
                dishes['ingridient_name'] = value[0]
                dishes['quantity'] = int(value[1])
                dishes['measure'] = value[2]
                cook_book[keys.strip()].append(dishes)
            empty_line = f.readline()
        # pprint(cook_book)
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
    # person_count = int(input('Введите количество персон:'))
    for dish in dishes:
        for ingredients in cook_book[dish]:
            menu = dict(ingredients)
            menu['quantity'] *= int(person_count)
            if menu['ingridient_name'] not in shop_list:
                shop_list[menu['ingridient_name']] = menu
            else:
                shop_list[menu['ingridient_name']]['quantity'] += menu['quantity']
    pprint(shop_list)
        # return shop_list
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



# with open('Cook_book.txt') as f:
#
#     from pprint import pprint
#
#     def get_cook_book():
#         cook_book = {}
#         for line in f:
#             keys = line
#             # print(keys.strip())
#             number = int(f.readline())
#             while number != 0:
#                 value = f.readline().strip().split('|')
#                 number -= 1
#                 # print(value)
#                 if keys.strip() not in cook_book.keys():
#                     cook_book[keys.strip()] = list()
#                 dishes = dict()
#                 dishes['ingridient_name'] = value[0]
#                 dishes['quantity'] = int(value[1])
#                 dishes['measure'] = value[2]
#                 cook_book[keys.strip()].append(dishes)
#             empty_line = f.readline()
#         # pprint.pprint(cook_book)
#         return cook_book

    # get_cook_book()

    # def get_shop_list_by_dishes(dishes, person_count):
    #     shop_list = {}
    #     cook_book = get_cook_book()
    #     # person_count = int(input('Введите количество персон:'))
    #     for dish in dishes:
    #         for ingredients in cook_book[dish]:
    #             menu = dict(ingredients)
    #             menu['quantity'] *= int(person_count)
    #             if menu['ingridient_name'] not in shop_list:
    #                 shop_list[menu['ingridient_name']] = menu
    #             else:
    #                 shop_list[menu['ingridient_name']]['quantity'] += menu['quantity']
    #     pprint(shop_list)
    #     # return shop_list
    # get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количетсва для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 8},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторятьс



# cook_book = {
#   'Омлет': [
#     {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
#     {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }