import platform
import subprocess
import time

enter=input("欢迎来带安全模式，重新启动请输入1，退出请输入2: ")
if enter=="1":
    subprocess.call(['python', 'PL-DOS-System.py'])
elif enter=="2":
    exit(0)
if enter=="3":
    if platform.system() == 'Linux':
        print('菜鸡玩儿，丨，一辈子也不支持，傻逼，南山少帅一伙的吧')
        time.sleep(2.5)
        exit()
    subprocess.call(['python', 'PL-DOS-Hardcore.py'])
