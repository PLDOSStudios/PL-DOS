import random, time

print('欢迎来到由BG-DOS团队制作的井字棋')
time.sleep(0.6)
print('1.创建一个新游戏')
print('任意键退出游戏')
a = input()
if a == '1':
    pass
else:
    quit()

game_map = ['[]', '[]', '[]',
            '[]', '[]', '[]',
            '[]', '[]', '[]']

column = 0
row = 0
number_list = [0, 1, 2]
block_list = [[0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8]]

while True:
    print(end='    ')
    print('0  1  2')
    print('+----------------------')
    for i in range(3):
        print('|', end = '')
        print(i, end='  ')
        for j in range(3):
            print(game_map[i * 3 + j], end = ' ')
        print()
    an = input().split()
    try:
        x = int(an[0])
        y = int(an[1])
    except:
        print('请输入规范的行号, 如 0 0')
        continue
    if len(an) != 2:
        print('请输入规范的行号, 如 0 0')
        continue
    elif x not in number_list or y not in number_list:
        print('请输入规范的行号, 如 0 0')
        continue
    else:
        game_map[y * 3 + x] = 'O'
        print(end='    ')
        print('0  1  2')
        print('+----------------------')
        for i in range(3):
            print('|', end='')
            print(i, end='  ')
            for j in range(3):
                print(game_map[i * 3 + j], end=' ')
            print()
        print()
        for i in range(8):
            if game_map[block_list[i][0]] == 'O' and game_map[block_list[i][1]] == 'O' and game_map[block_list[i][2]] == 'O':
                print('玩家赢了')
                break
            print('计算机思考中……')
            time.sleep(1.14514)
            while True:
                r = random.randint(0, 8)
                game_map[r] = 'X'
                break
            for i in range(8):
                if game_map[block_list[i][0]] == 'X' and game_map[block_list[i][1]] == 'X' and game_map[block_list[i][2]] == 'X':
                    print('计算机赢了')
                    break
