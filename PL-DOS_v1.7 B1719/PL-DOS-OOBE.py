import time
import os

def cls():
    os.system('cls')

print('嗨!别来无恙啊!')

time.sleep(0.7)
print('我们正在为你做准备')

time.sleep(1)
cls()

print('PL-DOS注册用户')
print('请输入你的用户名')
username = input()
print('请输入你的密码(如果不想设置输入None)')
userpass = input()
if userpass != 'None':
    print('请再次输入你的密码')
    userpass2 = input()
    if userpass == userpass2:
        print()
        print('你不好')
        time.sleep(1)
        os.system('cls')
        print('我们正在为你创建账号需要的东西')
        time.sleep(1)
        os.system('cls')
        print('这需要很长的时间')
        os.makedirs(fr'Users\{username}', exist_ok=True)
        with open(fr'Users\{username}\password.txt', 'w') as file:
            file.write(userpass)
        with open(fr'Users\{username}\autologin.txt', 'w') as file:
            file.write('0')
        os.makedirs(fr'Users\{username}\Note', exist_ok=True)
        time.sleep(2)
        os.makedirs(fr'Users\{username}\Game', exist_ok=True)
        with open(fr'Users\{username}\Game\card.txt', 'w') as file:
            file.write('999')
        os.system('cls')
        print('哦, 弄好了')
        time.sleep(1)
        os.system('cls')
        with open(r'System/DataFiles/user.txt', 'w') as f:
            e = f.write('1')
    else:
        print('你两次输入都不一样你设个嘚儿')
else:
    print('不设置密码可能会导致账号不安全!是否继续?[y/n]')
    aaaa = input()
    if aaaa == 'y':
        os.makedirs(fr'Users\{username}', exist_ok=True)
        with open(fr'Users\{username}\password.txt', 'w') as file:
            file.write('None')
        with open(fr'Users\{username}\autologin.txt', 'w') as file:
            file.write('0')
        print('完成了')
    elif aaaa == 'n':
        print('取消成功')