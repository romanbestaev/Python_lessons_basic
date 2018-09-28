#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class LotoBag:
    def __init__(self):
        self.barrels = [i for i in range(1,91)]
    def pull_barrel(self):
        b = random.choice(self.barrels)
        self.barrels.remove(b)
        print('Новый бочонок: {} (осталось {})'.format(b,len(self.barrels)))
        return b


class LotoCard:
    def __init__(self,name):
        self.status = 0
        self.name = name
        self.field = ['' for _ in range(9*3)]
        positions = []
        for x in range(3):
            positions.extend(random.sample(range(x*9,(x+1)*9),5))
        numbers = random.sample(range(1,91),15)
        for i in positions:
            self.field[i] = numbers.pop(0)
    
    def card_info(self):
        print(self.name)
        for i in range(3):
            print('%2s %2s %2s %2s %2s %2s %2s %2s %2s ' %
                  tuple(self.field[i*9:(i+1)*9]))
        print('--------------------------')
    
    def play(self, b, answer=None):
        if answer:
            if (answer=='y') and (b in self.field):
                self.field[self.field.index(b)]='-'
            elif (answer=='y') and (b not in self.field):
                self.status = -1
            elif (answer=='n') and (b not in self.field):
                pass
            elif (answer=='n') and (b in self.field):
                self.status = -1
            else:
                print('Не верное значение')
                self.status = -1
        else:
            if b in self.field:
                self.field[self.field.index(b)]='-'
        if(int not in list(map(type, self.field))):
            self.status = 1


LotoBagOne = LotoBag()

LotoCardUser = LotoCard('------ Ваша карточка -----')
LotoCardPC = LotoCard('-- Карточка компьютера ---')

while abs(LotoCardUser.status)+abs(LotoCardPC.status) == 0:
    b = LotoBagOne.pull_barrel()        
    LotoCardUser.card_info()
    LotoCardPC.card_info()
    LotoCardUser.play(b, input('Зачеркнуть цифру? (y/n):'))
#    LotoCardUser.play(b)
    LotoCardPC.play(b)
        
if LotoCardUser.status == 1:
    if LotoCardPC.status == 1:
        print('Ничья')
    else:
        print('Вы выйграли')
else:
    print('Вы проиграли')
