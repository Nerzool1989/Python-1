__author__: Канцеров Александр

import random
 class Card:
    def __init__(self, player):
        self.player = player
        self.nums = 15
        self.check = 0
        self.rows = []
        self.numbers = []
        
    def makecard(self):
        while len(self.numbers) < self.nums:
            number = random.randint(1, 90)
            if number not in self.numbers:
                self.numbers.append(number)
        self.rows = [sorted(self.numbers[:5]), sorted(self.numbers[5:10]),
                     sorted(self.numbers[10:])]
        
    def bingo(self, num):
        count = 0
        for row in self.rows:
            if num in row:
                row[row.index(num)] = 'X'
                count = 1
                self.check += 1
                break
        if count != 1:
            print(f'{self.player} проиграл!')
    
    def pullbarrel(self, num):
        for row in self.rows:
            if num in row:
                return True
        return False
    
    def printcard(self):
        cardname = f'-----{self.player}-----'
        print(cardname)
        for row in self.rows:
            for num in row:
                print(f' {num} ', end = '')
            print()
        print(f'Незачеркнуто номеров: {15 - self.check}')
        print('-' * len(cardname))
    
class Bot:
    def __init__(self, name, card):
        self.card = card
        self.name = name
    
    def action(self, num):
        if self.card.pullbarrel(num):
            self.card.bingo(num)
        else:
            print('Не зачеркиваю.')
    
start = input('Хотите сыграть в игру? Y/N: \n').upper()
if start == 'Y':
    Player = Card(input('Введите ваше имя: \n'))
    botname = input('Введите имя противника: \n')
    bot = Bot(botname, Card(botname))
 while start == 'Y':
    bot.card.makecard()
    Player.makecard()
    barrels = [x for x in range(1, 91)]
    
    while Player.check < 15 and bot.card.check < 15:
        print(f'В мешке осталось {len(barrels)} бочонков')
        Player.printcard()
        bot.card.printcard()
        barrel = random.choice(barrels)
        print(f'Бочонок № {barrel}')
        barrels.remove(barrel)
        choice = input('Хотите зачеркнуть номер? Y/N: \n').upper()
        
        if choice == 'Y':
            if not Player.pullbarrel(barrel):
                print('Этого номера нет на вашей карте. Вы проиграли.')
                print(f'В мешке остались бочонки: {barrels}')
                break
            Player.bingo(barrel)
        else:
            if Player.pullbarrel(barrel):
                print('У вас есть такой номер. Вы проиграли.')
                print(f'В мешке остались бочонки: {barrels}')
                break
        
        print(f'Очередь игрока {bot.name}')
        bot.action(barrel)
        if Player.check >= 15 and bot.card.check >= 15:
            print('Ничья!')
            print(f'В мешке остались бочонки: {barrels}')
        elif Player.check >=15:
            print(f'Победил {Player.player}')
            print(f'В мешке остались бочонки: {barrels}')
        elif bot.card.check >= 15:
            print(f'Победил {bot.name}')
            print(f'В мешке остались бочонки: {barrels}')
    
    start = input('Хотите сыграть еще раз? Y/N: \n').upper()
    
print('Спасибо за игру!')
