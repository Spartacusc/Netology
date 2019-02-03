
from contextlib import contextmanager
from timeit import default_timer as timer

@contextmanager
def my_time(file_path):
    try:
        start = timer()
        print(start)
        yield start
    finally:
        end = timer()
        print(end)
        print(end - start)

with my_time('Cook_book.txt') as start:
    with open('Cook_book.txt') as f:

        def get_cook_book():
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
            print(cook_book)
        get_cook_book()

# @contextmanager
# def my_open(file_path):
#     try:
#         file = open(file_path, 'r')
#         yield file
#     finally:
#         file.close()
#
# with my_time('test') as start:
#     with my_open('test') as file:
#         f = file.read()
#         f_1 = file.readline()
#         f_2 = file.readline()
#         print(f_2)
#         print(f)

# start = timer()
# print(start)
# print('hello')
# end = timer()
# print(end)
# print(end - start)