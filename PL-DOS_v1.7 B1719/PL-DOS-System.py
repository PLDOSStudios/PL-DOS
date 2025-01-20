import random
import sys, os, json
from datetime import datetime
import cmd
import subprocess
import psutil
import tkinter as tk
from tqdm import tqdm
import time

try:
    import signal
except ModuleNotFoundError:
    os.system("pip install psutil")
    os.system("pip install signal")
    os.system("pip install tqdm")
    import signal

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[36m'
RESET = '\033[0m'
WHITE = '\033[0m'
PURPLE_RED = '\033[35m'
ORANGE = '\033[38;2;255;165;0m'
BLUE = '\033[34m'

import os
import sys

file_path = "D:\桌面\运行补丁.cj "# 将这里替换为实际的文件路径

if not os.path.exists(file_path):
    print(f"运行许可不生效")
    sys.exit(1)

with open("PL\\pl.txt", "rb") as file:
    pldos = file.read().decode('utf-8')
    print(pldos, end = '')
print("轻于外，精于内")
huida=input("你是Linux用户吗？（y/n）:")
if huida == "y":
    print("你很诚实！傻逼，就是你，你还用Linux干嘛呢，不用Windows（或者未来的鸿蒙PC）")
    time.sleep(1)
    exit()
time.sleep(1)
import platform


print("正在加载...")
time.sleep(1)
for i in tqdm(range(100)):
    time.sleep(0.001)
if platform.system() == 'Linux':
    print('菜鸡玩儿，丨，一辈子也不支持，傻逼，给南山少帅一伙的吧')
    time.sleep(2.5)
    exit()
else:
    print("恭喜你，已通过防小可爱测试")
    time.sleep(2.5)
if platform.system() == 'Mac':
    print("找BG-DOSMac版去，小心我把你整亖")
time.sleep(0.4)
print("欢迎使用")
time.sleep(1)

current_path = os.getcwd()

directory = 'Users'
user_name = ''

class PLDOS(cmd.Cmd):
    os.system('cls')

    with open(r'System/DataFiles/user.txt', 'r') as f:
        e = f.read()
        if e == '0':
            print('你还没有注册')
            subprocess.call(['python', 'PL-DOS-OOBE.py'])
    entries = os.listdir(directory)
    folders = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]

    foo = 1
    for fo in folders:
        print(f"[{foo}] {fo}")
        foo += 1
    print('[114514] 注册账户')

    print('请选择要登录的用户')
    fooo = input()
    try:
        fooo = int(fooo)
        try:
            user_name = folders[fooo - 1]
        except:
            if fooo != 114514:
                print('你输入的不正确!!!!')
                subprocess.call(['python', '安全.py'])
            else:
                subprocess.call(['python', 'PL-DOS-OOBE.py'])
        else:
            if fooo <= foo:
                with open(f'Users/{folders[fooo - 1]}/autologin.txt', 'r', encoding='utf-8') as f:
                    ff = f.read()
                    if ff == '0':
                        with open(f'Users/{folders[fooo - 1]}/password.txt', 'r', encoding='utf-8') as f:
                            passsword = f.read()
                        if passsword != 'None':
                            print('请输入密码')
                            passs = input()
                            if passs != passsword:
                                print('密码错误!')
                                print('即将退出!')
                                time.sleep(2)
                                subprocess.call(['python', '安全.py'])
                            else:
                                print('密码正确!')
                        else:
                            print('没有密码，登录成功')
                    else:
                        print('自动登录成功!')

    except TypeError:
        print(f'{RED}[Error 18]{RESET} 你输入的不是数字!')
    except ValueError:
        print(f'{GREEN}[error 18]{RESET} 给老子乖点')
        time.sleep(1)
        subprocess.call(['python', '安全.py'])


    print('Welcome to PL-DOS')
    print('欢迎来到 PL-DOS')

    with open('System/Temp/now_user.txt', 'w') as f:
        f.write(user_name)

    words = ['输入help可以查看所有命令哦', 'PL-DOS 的全称是 Powerful Disk Operating System',]
    print(f'{CYAN}<你知道吗>{RESET} {random.choice(words)}')
    print(f'{CYAN}<你知道吗>{RESET} CANDOS的解散日期是8月17日，是BG工作室的诞生之日{RESET}')
    print(f'{RED}<请不要忘记!>{BLUE} 新中国成立前牺牲了{RED}370{BLUE}多万革命先烈!{BLUE}')

    prompt = f'PL-DOS{ORANGE}@{user_name}{RESET}>'
    input_cmd = ''
    #下方do_xxx 检测输入xxx时自动执行无需调用
    def do_help(self, arg):
         with open('System/help.txt','r', encoding = 'utf-8') as f:
             for line in f:
                 print(line, end = '')
         print()

    def do_english(self,arg):
        with open('PL-DOS-English.py',"rb") as file:
            english = file.read().decode('utf-8')
        exec(english)

    def do_about(self, arg):
        print('PL-DOS(Powerful-DOS)')
        print('我们的开发成员:')
        print('B站/QQ名:')
        print('BG-DOS工作室')
        print('东风Cherrier账号')
        print('yzklpy')
        print('PL系列工作室')
        print('QQ群:1005109089')

    def do_web(self,arg):
        with open("App/浏览.py","rb") as file:
            web=file.read().decode('utf-8')
        exec(web)

    def do_download(self,arg):
        with open("App/下崽器.py","rb") as file:
            download=file.read().decode('utf-8')
        exec(download)

    def do_pls(self,arg):
        with open("PLS 0.0.7/PLS 0.0.7/Powerful_Script.py","rb") as file:
            pls = file.read().decode('utf-8')
        exec(pls)

    def do_musicmaker(self, arg):
        with open("App/BGMusicMaker/music.py", "rb") as file:
            minesweeper = file.read().decode('utf-8')
        exec(minesweeper)
    def do_hello(self,arg):
        with open("App/hello.py","rb") as file:
             hello= file.read().decode('utf-8')
        exec(hello)

    def do_unpack(self,arg):
        print("你要压缩还是解压zip？\n[1]解压\n[2]压缩")
        jieguo = input()
        if jieguo == '1':
            subprocess.call(['python', 'App/解压.py'])
        if jieguo == '2':
            subprocess.call(['python', 'App/压缩.py'])

    def do_game(self,arg):
        print("正在准备")
        time.sleep(0.001)
        subprocess.call(['python', 'PL-GAME-System.py'])


    def do_snake(self,arg):
        with open("App/snake.py","rb") as file:
            snake = file.read().decode('utf-8')
        exec(snake)

    def do_shan(self,arg):
        with open("App/丧尸.py","rb") as file:
            shan = file.read().decode('utf-8')
        exec(shan)

    def do_minesweeper(self, arg):
        with open("App/minesweeper.py", "rb") as file:
            minesweeper = file.read().decode('utf-8')
        exec(minesweeper)

    def do_sb(self,arg):
        with open("App/赌博.py","rb") as file:
            sb = file.read().decode('utf-8')
        exec(sb)

    def do_exit(self, arg):
        print('再见')
        exit()

    def do_cls(self, arg):
        os.system('cls')

    def do_users(self, arg):
            directory = 'Users'
            entries = os.listdir(directory)
            folders = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]
            print()
            print('   用户名          权限')
            print('+---------------------------------------')
            for i in folders:
                if i == '114514':
                    print(f'|  114514          开发者')
                elif i == 'Guest':
                    print(f'|  Guest           访客')
                else:
                    print(f'|  {i}{(8-len(i))*' '}        管理员')

    def do_tictactoe(self, arg):
        print('你要运行哪一个\n[1] 新版井字棋\n[2] 第二版井字棋\n[3] 老六版井字棋')
        eeq = input()
        if eeq == '1':
            subprocess.call(['python', 'App/TICTACTOE.PY'])
        elif eeq == '2':
            subprocess.call(['python', 'App/TICTACTOE2.PY'])
        elif eeq == '3':
            subprocess.call(['python', 'App/TICTACTOEOLD.PY'])

    def do_card(self, arg):
        subprocess.call(['python', 'App/CARD.PY'])


    def do_dir(self, arg):
        dir_path = 'System'
        for item in os.listdir(dir_path):
            full_path = os.path.join(dir_path, item)
            if os.path.isfile(full_path):
                print(full_path)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                print(os.path.join(root, file))

    def do_pymm(self, arg):
        subprocess.call(['python', 'Pymm/pymm.py'])

    def do_notepad(self, arg):
        subprocess.call(['python', 'App/Notepad.py'])

    def do_hardcore(self, arg):
        subprocess.call(['python', 'PL-DOS-Hardcore.py'])

    def do_autologin(self, arg):
        while True:
            user_name = input('请输入用户名')
            if user_name == 'quit':
                quit()
            try:
                with open(current_path + f"\\Users\\{user_name}\\password.txt"):
                    pass
            except FileNotFoundError:
                print('[Error 4] 找不到指定用户!')
                continue
            user_password = input('请输入密码')
            with open(fr'Users\{user_name}\password.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                if content == user_password:
                    break
                else:
                    print('[Error 5] 密码错误!')
        with open(f'Users/{user_name}/autologin.txt', 'w') as fie:
            fie.write('1')
        print('修改设置成功!')

    def do_explorer(self, arg):
        subprocess.call(['python', 'App/Explorer.py'])

    def do_store(self, arg):
        subprocess.call(['python', 'PLStore.py'])

    def do_applist(self, arg):
        directory = r'UsersApp'
        for item in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, item)):
                print(item)
        print('请输入要运行的软件(区分大小写)')
        aaaa = input()
        try:
            subprocess.call(['Python', fr'UsersApp\{aaaa}\{aaaa}.py'])
        except:
            print('找不到目标app')

    def do_restart(self, arg):
        subprocess.call(['python', 'PL-DOS-System.py'])
        quit()

    def do_antivirus(self, arg):
        subprocess.call(['python', r'main.py'])

    def default(self, line):
        try:
            self.input_cmd = line
            re = eval(self.input_cmd)
            print(re)
        except:
            print(f'{RED}[Error 12]{RESET} 命令不存在')

PLDOS().cmdloop()
