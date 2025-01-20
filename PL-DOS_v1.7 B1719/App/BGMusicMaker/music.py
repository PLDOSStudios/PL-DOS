import random
import time
from datetime import datetime
from tkinter import messagebox
import subprocess
import os
try:
    from musicpy import *
except ModuleNotFoundError:
    os.system('pip install musicpy')
    from musicpy import *

def name_error():
    global lines
    print('name_error变量名错误: 在第' + str(lines) + '行, 在变量名开头应为字母而不是数字,并没有特殊符号和中文')


def start():
    global lines
    lines += 1
    c = input('<Pymm-' + str(lines) + '>')
    b.append(c.split())
    if c == 'end':
        run()
    elif c == 'exit':
        return

    if c == 'restart':
        lines = 0
        print('------------------------------------RESTART----------------------------------------------')
        b.clear()
        v.clear()
    start()


def run():
    global b, v, cch, lines, music_speed, yin
    d = 0
    co = 0
    cch = []
    loop = 0
    ln = 0
    for i in b:
        loop += 1
        if i[0] == '@':
            if i[1] == 'set':
                if i[2] == 'speed':
                    try:
                        music_speed = int(i[3])
                    except ValueError:
                        print('speed变量值错误: 不是数字')
                        continue
                    print(f'速度设置成功, 当前速度{music_speed}')
                elif i[2] == 'default':
                    try:
                        music_speed = 60
                    except ValueError:
                        print('speed变量值错误: 不是数字')
                        continue
                    print(f'速度设置成功, 当前速度{music_speed}')
            if i[1] == 'loader':
                if i[2] == 'save':
                    if i[3] == 'after':
                        try:
                            with open(input('请输入保存路径') + '.bgmusic', 'w', encoding='UTF-8') as f:
                                for i in b:
                                    f.write(' '.join(i))
                                    f.write('\n')
                        except IndexError:
                            print('没有输入路径')
                            continue
                elif i[2] == 'load':
                    try:
                        with open(input('请输入读取路径') + '.bgmusic', 'r', encoding='UTF-8') as f:
                            b.clear()
                            for line in f:
                                b.append(line.strip().split())
                    except FileNotFoundError:
                        print('找不到该文件')
                        continue
                else:
                    print('loader命令不存在')


        if len(i) > 1:
            now = 0
            if len(i) != 16:
                print('输入不符合规定')
                continue
            for jjj in range(15):
                if len(i[jjj]) == 3:
                    if i[jjj][2] != '#' and i[jjj][2] != 'b':
                        print(f'输入不符合规定,因为升降调不正确')
                        continue
                    else:
                        selc = i[jjj][1]
                        sheng = i[jjj][2]
                        diao = i[jjj][0]
                        now = yin[selc]
                        if i[jjj + 1] != '-':
                            f_f = note(f'{yin[selc]}{sheng}{diao}', int(diao), duration=(60 / music_speed) * 0.25)
                        else:
                            for iiiii in range(15, 0, - 1):
                                if jjj < iiiii and i[jjj + (16 - iiiii)] == '-':
                                    f_f = note(f'{yin[selc]}{sheng}{diao}', duration=(60 / music_speed) * (0.25 + 0.25 * (16 - iiiii)))
                                else:
                                    break
                        print(f'演奏音符{selc}{sheng}')
                        play(f_f, wait=True)
                if len(i[jjj]) == 2:
                    selc = i[jjj][1]
                    diao = i[jjj][0]
                    now = yin[selc]
                    if i[jjj + 1] != '-':
                        f_f = note(f'{yin[selc]}', int(diao), duration=(60 / music_speed) * 0.25)
                    else:
                        for jjjjj in range(15, 0, -1):
                            if jjj < jjjjj and i[jjj + (16 - jjjjj)] == '-':
                                f_f = note(f'{now}', int(diao), duration=(60/music_speed) * (0.25 + 0.25 * (16 - jjjjj)))
                            else:
                                break
                    print(f'演奏音符{selc}')
                    play(f_f, wait=True)
                if len(i[jjj]) == 1:
                    if i[jjj] == '0':
                        time.sleep(0.25)


    print('运行结束啦!')
    lines = 0


lines = 0
b = []
cch = []
v = {}
music_speed = 60
music_beat = 4
yin = {'1':'C', '2':'D', '3':'E', '4':'F', '5':'G', '6':'A', '7':'B'}
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
name = ['pr', 'int', 'if', 'else', 'endif', 'end', 'var', 'en', 'ok', 'help', 'start']
print('正在启动编译器……')
time.sleep(1)
print('PymmMusicMaker 2024/10/24')
while True:
    current_path = os.getcwd()
    a = input('PymmMusic-Shell>')
    if a == 'start':
        start()
        break
    elif a == 'exit':
        break
    elif a == 'help':
        with open(current_path + "\\Disks\\A\\BG_SYSTEM\\BIN\\指令说明.txt", "r", encoding="utf-8") as menu:
            for text in menu.readlines():
                print(text, end='')
            print()
    elif a == 'open':
        print('请输入要打开的文件, .pymmmusic会自动添加')
        file = input('>')
        if file[-10:] != '.pymmmusic':
            file += '.pymmmusic'
        try:
            with open(file, 'r', encoding='UTF-8') as f:
                b.clear()
                for line in f:
                    b.append(line.strip().split())
                run()
        except FileNotFoundError:
            print('找不到该文件')