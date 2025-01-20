import os
try:
    import requests
    import shutil
except ImportError:
    os.system('pip install requests')
    os.system('pip install shutil')
e = []
b = []
print('欢迎使用BG-DOS 商店 v1.0')
while True:
    def download_file():
        global download_dir, filename, choice
        response = requests.get(url)
        if response.status_code == 200:
            if choice[0] == 'A' or choice[0] == 'C':
                os.makedirs(f'UsersApp/{filename}', exist_ok=True)
                with open(f'UsersApp/{filename}/{filename + '.py'}', 'wb') as file:
                    file.write(response.content)
                print(f'文件已下载并保存到 UsersApp/{filename}')
            elif choice[0] == 'B':
                with open(f'{download_dir}/{filename}.exe', 'wb') as file:
                    file.write(response.content)
                print(f'文件已下载并保存到 {download_dir}')
        else:
            print(f'下载失败，状态码：{response.status_code}')

    print('特别感谢:飞流云盘https://pc.feiliupan.com/提供存储服务')

    with open('System/Store/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            e = []
            for word in line.split():
                e.append(word)
            b.append(e)

    apps = {}
    app_name = {}

    for i in b:
        print(f'[{i[0]}] {i[1]}')
        apps.update({i[0]: i[2]})
        app_name.update({i[0]: i[3]})

    download_dir = 'Downloads'

    choice = input('请输入要下载的应用程序编号：')
    if choice in apps:
        url = apps[choice]
        filename = app_name[choice]
        download_file()