import random, json


def shuffle_and_prepare_cards():
    # 定义一副牌，每张牌有匹配的伙伴
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
    random.shuffle(cards)  # 随机打乱牌的顺序
    return cards


def display_cards(cards, revealed):
    # 显示当前牌的布局
    for i in range(len(cards)):
        if revealed[i]:
            print(cards[i], end=" ")
        else:
            print("_", end=" ")
        if (i + 1) % 4 == 0:  # 每4张牌换行
            print()
    print()


def play_game():
    cards = shuffle_and_prepare_cards()
    revealed = [False] * len(cards)  # 初始所有牌未被揭示
    first_pick = None
    second_pick = None
    moves = 0

    while not all(revealed):
        display_cards(cards, revealed)

        # 玩家选择第一张牌
        if first_pick is None:
            first_pick = int(input("选择第一张牌的位置 (0-7): "))
            while first_pick < 0 or first_pick >= len(cards) or revealed[first_pick]:
                first_pick = int(input("无效位置，请重新选择 (0-7): "))
            revealed[first_pick] = True
            moves += 1
        # 玩家选择第二张牌
        else:
            second_pick = int(input("选择第二张牌的位置 (0-7): "))
            while second_pick < 0 or second_pick >= len(cards) or revealed[second_pick] or second_pick == first_pick:
                second_pick = int(input("无效位置，请重新选择 (0-7): "))
            revealed[second_pick] = True
            moves += 1
            # 判断两张牌是否匹配
            if cards[first_pick] == cards[second_pick]:
                first_pick = None
                second_pick = None
            else:
                revealed[first_pick] = False
                revealed[second_pick] = False
                first_pick = None
                second_pick = None
                print("不匹配，牌被翻回。")

    display_cards(cards, revealed)
    with open(r'System/Temp/now_user.txt', 'r') as file:
        nowuser = file.read()
    print("你赢了！总移动次数：", moves)
    with open(rf'Users/{nowuser}/Game/card.txt', 'r') as file:
        high = file.read()
    high = int(high)
    if high > moves:
        with open(fr'Users/{nowuser}/Game/card.txt', 'w') as file:
            file.write(str(moves))
    print('历史最高纪录:', high)
play_game()