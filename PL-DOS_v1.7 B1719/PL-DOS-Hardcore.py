import random
import time, sys, os, json
import datetime
try:
    import psutil
    import shutil
    from colorama import Fore, init
except ModuleNotFoundError:
    os.system("pip install psutil")
    os.system("pip install shutil")
    os.system("pip install colorama")
    import psutil
    from colorama import Fore, init

num_list = ['0', '1', '2', '3', '4', '5', '6', '7']

os.system(r'title PL-DOS 1.x Hardcore')

time.sleep(1)
current_path = os.getcwd()
print('PL-DOS硬核CMD, 用于运行内测应用与高级设置')

def print_tree(dir_path, prefix=''):
    if not os.path.isdir(dir_path):
        return

    files = os.listdir(dir_path)
    for i, file in enumerate(files):
        print(prefix + '├── ' + file)
        path = os.path.join(dir_path, file)
        if os.path.isdir(path):
            if i == len(files) - 1:
                new_prefix = prefix + '    '
            else:
                new_prefix = prefix + '|   '
            print_tree(path, new_prefix)

while True:
    cmd = input(fr'PL-DOS\HARDCORE_CMD A:\\')
    match cmd.lower():
        case 'mv':
            print('请输入要移动的文件路径')
            a = input()
            print('请输入要移动文件的目标路径')
            b = input()
            try:
                shutil.move(a, b)
            except:
                print('移动时出现错误')

        case 'md':
            print('请输入要创建文件夹的路径')
            c = input()
            print('请输入文件夹名')
            d = input()
            try:
                os.makedirs(fr'{c}\{d}', exist_ok=True)
            except:
                print('创建文件夹时出错')

        case 'type':
            print('请输入要打开的文件路径')
            g = input()
            try:
                with open(g, 'r', encoding='utf-8') as file:
                    h = file.readlines()
                    for i in h:
                        print(i)
            except:
                print('读取文件时出错')

        case 'dir':
            dir_path = 'System'
            for item in os.listdir(dir_path):

                full_path = os.path.join(dir_path, item)

                if os.path.isfile(full_path):
                    print(full_path)
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    print(os.path.join(root, file))


        case 'help':
            with open(current_path + "\\System\\help.txt", "r", encoding="utf-8") as menu:
                for text in menu.readlines():
                    print(text, end = '')
                print()

        case 'cd':
            print(r'BG-DOS\HARDCORE_CMD A:\\')

        case 'date':
            today = datetime.date.today()
            weekday_index = today.weekday()
            weekdays = ["一", "二", "三", "四", "五", "六", "日"]
            weekday_name = weekdays[weekday_index]
            print(f'当前日期: {today.year}/{today.month}/{today.day} 周{weekday_name}')

        case 'cls':
            os.system('cls')

        case 'time':
            now = datetime.now()
            print(f'当前时间: {now.hour}:{now.minute}:{now.second}')

        case 'vol':
            print('驱动器 A')
            print('驱动器 A 中的卷是 BGDOS-SYSTEM')
            print('卷的序列号是 1145-250B')

        case 'musicmaker':
            with open(current_path + "\\App\\BGMusicMaker\\music.py", "rb") as file:
                cardold = file.read().decode('utf-8')
            exec(cardold)

        case 'title':
            print('请输入要设置的标题')
            ttt = input()
            os.system(f'title {ttt}')

        case 'tree':
            print_tree('.')

        case 'rd':
            print('请输入你要删除的目录')
            a = input()
            try:
                os.remove(a)
            except:
                print('删除目录发生错误')

        case 'cp':
            print('请输入你要复制的文件路径')
            cp1 = input()
            print('请输入你要复制的目标文件路径')
            cp2 = input()
            try:
                shutil.copy2(cp1, cp2)
                print(f'成功从 {cp1} 复制到 {cp2}')
            except:
                print('复制不了,肯定是你的问题!')