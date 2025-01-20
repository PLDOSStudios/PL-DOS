import random

com_s = 0
pla_s = 0
while True:
    choices = ['石头', '剪刀', '布']
    a = input('请输入数字：1石头 2剪刀 3布 4退出')
    try:
        a = int(a)
    except:
        print('谁让你不输入数字的, 该罚!')
        continue
    if a not in [1, 2, 3, 4]:
        print('谁让你不输入选项的, 该罚!')
    elif a == 4:
        break
    else:
        computer_ch = random.randint(1, 3)
        if (a == 1 and computer_ch == 2) or (a == 2 and computer_ch == 3) or (a == 3 and computer_ch == 1):
            print('玩家赢了')
            play = choices[a - 1]
            comp = choices[computer_ch - 1]
            print(f'玩家出了{play}, 计算机出了{comp}')
            pla_s += 1
            print(f'比分{pla_s}:{com_s}')
            continue
        if (a == 2 and computer_ch == 1) or (a == 3 and computer_ch == 2) or (a == 1 and computer_ch == 3):
            print('计算机赢了')
            play = choices[a - 1]
            comp = choices[computer_ch - 1]
            print(f'玩家出了{play}, 计算机出了{comp}')
            com_s += 1
            print(f'比分{pla_s}:{com_s}')
            continue
        if a == computer_ch:
            print('平局')
            play = choices[a - 1]
            comp = choices[computer_ch - 1]
            print(f'玩家出了{play}, 计算机出了{comp}')
            print(f'比分{pla_s}:{com_s}')