import random

print('欢迎来到由BG-DOS团队@颠佬没了开发的老六纸牌')
print('你要凑到114点, J = 11, Q = 15, K = 25')

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 15, 'K': 25,}

all_cards = []

for i in range(8):
    for j in cards:
        all_cards.append(j)

random.shuffle(all_cards)

computer_point = random.randint(100, 120)
player_point = 0
player_card = 0

while True:
    print(f'玩家点数: {player_point}')
    print('玩家请摸牌')
    a = input('是否抢牌:(1)拿来吧你, (2)停牌')
    if a != '1' and a != '2':
        print('你在干什么?!')
        print('你这样我们只好出手了')
        player_point = 114514
        print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
        print('计算机赢了')
        break
    elif a == '1':
        player_card = all_cards[random.randint(0, 95)]
        print(f'你摸到了 {player_card}')
        player_point += card_points[player_card]
    elif a == '2':
        if player_point > 114:
            print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
            print('你超过114了, 该罚!')
            break

        elif computer_point > 114:
            print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
            print('玩家赢了')
            break

        if player_point == 114:
            print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
            print('玩家赢了')
            break
        if computer_point == 114:
            print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
            print('计算机赢了')
            break

        if 114 - player_point > 114 - computer_point:
            print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
            print('计算机赢了')
            break

        elif 114 - player_point < 114 - computer_point:
            print(f'玩家点数: {player_point}    计算机点数: {computer_point}')
            print('玩家赢了')
            break

        elif player_point == computer_point:
            print('平局')
            break
