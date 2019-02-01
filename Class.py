

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food = 1

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def collect(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    def __add__(self, other):
         return self.weight + other.weight


    def __lt__(self, other):
        return self.weight < other.weight


class Cow(Animal):
    milk = 1

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        '''кормим животное'''
        if self.food:
            self.food = 0
            print('Животное голодно -', self.name.title())
            return self.food
        else:
            print('Уже покормили -', self.name.title())

    def collect(self):
        if self.milk:
            self.milk = 0
            print('Пора доить', self.name.title())
            return self.milk
        else:
            print('Подоили', self.name.title())

    def voice(self):
        print('Мууу')

class Goat(Cow):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def voice(self):
        print(self.name.title(), 'Меее')

class Chicken(Animal):
    eggs = 1

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        '''кормим животное'''
        if self.food:
            self.food = 0
            print('Животное голодно -', self.name.title())
            return self.food
        else:
            print('Уже покормили -', self.name.title())

    def collect(self):
        if self.eggs:
            self.eggs = 0
            print('Пора собирать яйца', self.name.title())
            return self.eggs
        else:
            print('Собрали яйца у', self.name.title())

    def voice(self):
        print(self.name.title(), 'Кококо')

class Duck(Chicken):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def voice(self):
        print(self.name.title(), 'КряКря')

class Goose(Chicken):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def voice(self):
        print(self.name.title(), 'Гагага')

class Sheep(Animal):
    cut = 1

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        '''кормим животное'''
        if self.food:
            self.food = 0
            print('Животное голодно -', self.name.title())
            return self.food
        else:
            print('Уже покормили -', self.name.title())

    def collect(self):
        '''Подстригаем овцу'''
        if self.cut:
            self.cut = 0
            print('Пора стричь', self.name.title())
            return self.cut
        else:
            print('Постригли', self.name.title())

    def voice(self):
        print(self.name.title(), 'Бее')


cow = Cow('мурка', 500)

goat_0 = Goat('рога', 100)

goat_1 = Goat('копыта', 100)

sheep_0 = Sheep('барашек', 40)

sheep_1 = Sheep('кудрявый', 45)

chicken_0 = Chicken('коко', 1)

chicken_1 = Chicken('кукареку', 2)

duck = Duck('кряква', 5)

goose_0 = Goose('серый', 15)

goose_1 = Goose('белый', 20)

animal_list = [cow, goat_0, goat_1, sheep_0, sheep_1, chicken_0, chicken_1, duck, goose_0, goose_1]

summa = sum(animal.weight for animal in animal_list)
print('Суммарный вес равен - ', summa)

# почему тоже самое через for не получилось
# for animal in animal_list:
#     summ = sum(animal.weight)
# print(summ)

def weight():
    weight = 0
    name = None
    for animal in animal_list:
        if animal.weight > weight:
            weight = animal.weight
            name = animal.name
    print('Имя самого тяжелого животного - ', name.title())

weight()
def collect_amimal():
    for animal in animal_list:
        animal.collect()

collect_amimal()
collect_amimal()

def feed_animal():
    for animal in animal_list:
        animal.feed()

feed_animal()
feed_animal()

