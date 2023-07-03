#
# #Задание 1.
# num = input("Введите 5 чисел через запятую: ")
# numbers = num.split(",")
#
# numbers = list(float(num) for num in numbers)
# sred = sum(numbers) / len(numbers)
# print("Среднее арифметическое: ", sred)
#
# #Задание 2.
#
# import math
# rad = int(input('Введи радиус круга:\n'))
# s = math.pi * rad **2
# print('Площаддь круга равна ', s)

#Задание 3.
# import math
# def krug(radius):
#     return math.pi * radius ** 2
#
# def pr_ygolnik(width, height):
#     return width * height
#
# def oval(radius1, radius2):
#     return math.pi * radius1 * radius2
#
# def romb(diag1, diag2):
#     return (diag1 * diag2) / 2
#
# def trapeci(a1, a2, height):
#     return ((a1 + a2) * height) / 2
#
# def main():
#     print("Выберите фигуру для вычисления площади:")
#     print("1. Круг")
#     print("2. Прямоугольник")
#     print("3. Овал")
#     print("4. Ромб")
#     print("5. Трапеция")
#
#     choice = int(input("Введите номер фигуры: "))
#
#     if choice == 1:
#         radius = int(input("Введите радиус круга: "))
#         area = krug(radius)
#     elif choice == 2:
#         width = int(input("Введите ширину прямоугольника: "))
#         height = int(input("Введите высоту прямоугольника: "))
#         area = pr_ygolnik(width, height)
#     elif choice == 3:
#         radius1 = int(input("Введите радиус 1 овала: "))
#         radius2 = int(input("Введите радиус 2 овала: "))
#         area = oval(radius1, radius2)
#     elif choice == 4:
#         diag1 = int(input("Введите диагональ 1 ромба: "))
#         diag2 = int(input("Введите диагональ 2 ромба: "))
#         area = romb(diag1, diag2)
#     elif choice == 5:
#         a1 = int(input("Введите длину основания 1 трапеции: "))
#         a2 = int(input("Введите длину основания 2 трапеции: "))
#         height = int(input("Введите высоту трапеции: "))
#         area = trapeci(a1, a2, height)
#     else:
#         print("Ошибка: Неправильный выбор")
#
#     print("Площадь выбранной фигуры:", area)
#
# main()

#Задание 4.
# import random
# names = ['Паша', 'Гена', 'Юра', 'Леша', 'Катя', 'Надя', 'Варя', 'Андрей', 'Вова', 'Валера']
# gorod = ['Оренбург', 'Псков', 'Феодосия', 'Дно', 'Остров', 'Питер', 'Москва', 'Кашира', 'Волгоград', 'Ростов']
# pro = ['Электрик', 'Тестер', 'Девопс', 'Менеджер', 'Грохотовщик', 'Моряк', 'Юрист', 'Врач', 'Вахтер', 'Ген.Дир']
#
# ran_names = random.sample(names, len(names))
# ran_gorod = random.sample(gorod, len(gorod))
# ran_pro = random.sample(pro, len(pro))
#
# dict_data = {}
#
# for i in range(len(ran_names)):
#     dict_data[ran_names[i]] = {'Город': ran_gorod[i], 'Профессия': ran_pro[i]}
#
# for name, info in dict_data.items():
#     print('Имя:', name)
#     print('Город:', info['Город'])
#     print('Профессия:', info['Профессия'])
#     print()
#Задание 5.
# import random
#
# comp = ''
# hum = ''
# turn = ['k', 'n', 'b']
# win = ['kn', 'nb', 'bk']
# loose = ['kb', 'nk', 'bn']
# draw = ['kk', 'nn', 'bb']
# score_hum = 0
# score_comp = 0
#
# def f1(x):
#     global hum, comp, score_hum, score_comp
#     hum = x
#     r = random.randint(0, 2)
#     comp = turn[r]
#     print(hum, comp)
#     print('человек', hum, ', робот', comp)
#     proverka()
#
# def f2():
#     global hum
#     hum = random.choice(turn)
#     r = random.randint(0, 2)
#     comp = turn[r]
#     print('человек', hum, ', робот', comp)
#     proverka()
#
# def proverka():
#     global score_hum, score_comp
#     result = hum + comp
#     if result in win:
#         print('pobeda')
#         score_hum += 1
#         print(' --вы победили!', score_hum, ':', score_comp)
#     elif result in loose:
#         print('ne povezlo')
#         score_comp += 1
#         print(' --робот победил!', score_hum, ':', score_comp)
#     else:
#         print('nichya')
#         print(' --ничья', score_hum, ':', score_comp)
#         s1()
#
# def s1():
#     pass
#
# f2()
import random
# suits = ['\u2664','\u2665','\u2666','\u2667']
# numbers = ['Tyz',2,3,4,5,6,7,8,9,10,'Valet','Dama','Korol']
# class Card:
#     def __init__(self,suit,val):
#         self.suit=suit
#         self.val=val
#     pass
#
#     def showcard(self):
#         print(self.suit,'-',self.val)
#
# class Koloda:
#     cards = []
#     def __init__(self):
#         for s in suits:
#             for n in numbers:
#                 self.cards.append(Card(s,n))
#
#     pass
#     def showdeck(self):
#         for c in self.cards:
#             # print(self.cards.index(c)+1)
#             c.showcard()
#             pass
#     def shuffle(self):
#             random.shuffle(self.cards)
#     def minuscarta(self):
#         return self.cards.pop()
# class Player:
#     def __init__(self,name):
#         self.name=name
#         self.hand=[]
#
#     def showhand(self):
#         for card in self.hand:
#             card.showcard()
#     def takecard(self,deck):
#         self.hand.append(deck.minuscarta())
#
#     pass
# # card1 = Card('крести','валет')
# # card1.showcard()
# deck1 = Koloda()
# deck1.shuffle()
# # deck1.showdeck()
# # c1 = deck1.minuscarta()
# # c1.showcard()
# # c2 = deck1.minuscarta()
# # c2.showcard()
# bob = Player('Bob')
# bob.takecard(deck1)
# bob.takecard(deck1)
# bob.showhand()
# print('###############################')
# boris = Player('Boris')
# boris.takecard(deck1)
# boris.takecard(deck1)
# boris.showhand()

#ДЗ
import random

suits = ['\u2664', '\u2665', '\u2666', '\u2667']
numbers = ['Tyz', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valet', 'Dama', 'Korol']


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def showcard(self):
        print(self.suit, '-', self.val)


class Koloda:
    cards = []

    def __init__(self):
        for s in suits:
            for n in numbers:
                self.cards.append(Card(s, n))

    def showdeck(self):
        for c in self.cards:
            c.showcard()

    def shuffle(self):
        random.shuffle(self.cards)

    def minuscarta(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def showhand(self):
        for card in self.hand:
            card.showcard()

    def takecard(self, deck):
        self.hand.append(deck.minuscarta())

    def f1 (self):
        sum_count = 0                                              #хранит сумму очков руки
        tyz_count = 0                                              # хранит количество тузов в руке
        for card in self.hand:
            if isinstance(card.val, int):                          # используется для проверки типа объекта
                sum_count += card.val
            elif card.val in ['Valet', 'Dama', 'Korol']:           #прибавляется 10
                sum_count += 10
            elif card.val == 'Tyz':
                sum_count += 11
                tyz_count += 1
        while sum_count > 21 and tyz_count > 0:
            sum_count -= 10                                       # если больше 21 и есть тузы убираем 10 очков
            tyz_count -= 1
        return sum_count


def game():
    deck = Koloda()                                               # Создаем колоду и перемешиваем
    deck.shuffle()

    player = Player('Игрок')                                      # Создаем игрока и компьютера
    computer = Player('Компьютер')

    for a in range(2):                                            # Игрок и компьютер берут по две карты
        player.takecard(deck)
        computer.takecard(deck)

    print("Карты игрока:")                                        # Показываем карты игрока (одну из двух)
    player.showhand()

    while True:                                                   # цикл для игрока
        choice = input("Берете еще карту? (да/нет): ")
        if choice.lower() == 'да':
            player.takecard(deck)
            print("Ваши карты:")
            player.showhand()
            if player.f1() > 21:
                print("Вы проиграли. Сумма ваших очков превысила 21.")
                return
        else:
            break

    while computer.f1() < 17:                         # Игровой цикл для компьютера
        computer.takecard(deck)
    print("Карты компьютера:\n")                      # Kарты компьютера
    computer.showhand()

    player_sum = player.f1()                        # Определяем победителя
    computer_sum = computer.f1()
    print("Сумма ваших очков:\n", player_sum)
    print("Сумма очков компьютера:", computer_sum)

    if player_sum > 21:
        print("Вы проиграли. Сумма ваших очков превысила 21.")
    elif computer_sum > 21:
        print("Вы выиграли. У компьютера сумма очков превысила 21.")
    elif player_sum == computer_sum:
        print("Ничья. У вас и компьютера одинаковая сумма очков.")
    elif player_sum > computer_sum:
        print("Вы выиграли. У вас больше очков, чем у компьютера.")
    else:
        print("Вы проиграли. У компьютера больше очков, чем у вас.")



game()
