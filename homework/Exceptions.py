operation = input ("Введите операцию: ")
oper = operation.split()

symbol = ['+', '-', '*', '/']

try:
    assert len(oper) < 4
except AssertionError:
    print('Введите три аргумента')
    exit()

try:
    assert oper[0] in symbol
except AssertionError:
    print('Такой операции нет')

try:
    assert int(oper[1]) >= 0 and int(oper[2]) >= 0
except AssertionError:
    print('Необходимо ввести положительные числа')
    exit()

if oper[0] == "+":
    try:
        print(int(oper[1]) + int(oper[2]))
    except ValueError:
        print('Необходимо ввести числа')
elif oper[0] == "-":
    try:
        print(int(oper[1]) - int(oper[2]))
    except ValueError:
        print('Необходимо ввести числа')
elif oper[0] == "*":
    try:
        print(int(oper[1]) * int(oper[2]))
    except ValueError:
        print('Необходимо ввести числа')
elif oper[0] == "/":
    try:
        print(int(oper[1]) / int(oper[2]))
    except ValueError:
         print('Необходимо ввести числа')
    except ZeroDivisionError:
         print('Вообще-то на ноль делить нельзя!!!')


documents = [
        {"type": "passport", "number": '2207 876234', "name": "Василий Гупкин"},
        {"type": "invoice", "number": '11-2', "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": '10006', "name": "Аристарх Павлов"}
      ]

def list(docs):
    keys = input("Введите имя ключа: ")
    for listik in docs:
        try:
            print(listik[keys])
        except KeyError:
            print('Такого ключа нет')
            break

list(documents)