class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food = 1

    def feed(self):
        '''кормим животное'''
        if self.food:
            self.food = 0
            print('Животное голодно -', self.name.title())
            return self.food
        else:
            print('Уже покормили -', self.name.title())

    def voice(self):
        '''голос'''
        print('Голос')

    def __add__(self, other):
         return self.weight + other.weight


    def __lt__(self, other):
        return self.weight > other.weight


class Cow(Animal):
    milk = 1

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_milk(self):
        if self.milk:
            self.milk = 0
            print('Пора доить')
            return self.milk
        else:
            print('Подоили', self.name.title())

    def voice(self):
        print('Мууу')

class Goat(Cow):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def voice(self):
        print('Меее')

class Chicken(Animal):
    eggs = 1

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_eggs(self):
        if self.eggs:
            self.eggs = 0
            print('Пора собирать яйца')
            return self.eggs
        else:
            print('Собрали яйца у', self.name.title())

    def voice(self):
        print('Кококо')

class Duck(Chicken):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def voice(self):
        print('КряКря')

class Goose(Chicken):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def voice(self):
        print('Гагага')

class Sheep(Animal):
    cut = 1

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def cut(self):
        '''Подстригаем овцу'''
        if self.cut:
            self.cut = 0
            print('Пора стричь')
            return self.cut
        else:
            print('Постригли', self.name.title())

    def voice(self):
        print('Бее')



cow = Cow('мурка', 500)
# cow.feed()
# cow.feed()
# cow.get_milk()
# cow.get_milk()
# cow.voice()

goat_0 = Goat('рога', 100)
# goat_0.feed()
# goat_0.get_milk()
# goat_0.voice()

goat_1 = Goat('копыта', 100)
# goat_1.feed()
# goat_1.get_milk()
# goat_1.voice()

sheep_0 = Sheep('барашек', 40)

sheep_1 = Sheep('кудрявый', 45)

chicken_0 = Chicken('коко', 1)
# chicken_0.feed()
# chicken_0.get_eggs()
# chicken_0.voice()

chicken_1 = Chicken('кукареку', 2)
# chicken_1.feed()
# chicken_1.get_eggs()
# chicken_1.voice()

duck = Duck('кряква', 5)

goose_0 = Goose('серый', 15)

goose_1 = Goose('белый', 20)


# print(cow.__dict__)
# print(Animal.__dict__)


# print(cow.weight + duck.weight)
# print(cow + duck + goat_0)
