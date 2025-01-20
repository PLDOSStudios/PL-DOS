import os
try:
    import requests
    import shutil
except ImportError:
    os.system('pip install requests')
    os.system('pip install shutil')

def download_file(filename, url, download_dir):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{download_dir}/{filename + '.py'}', 'wb') as file:
            file.write(response.content)
        print(f'文件已下载并保存到 {download_dir}/{filename}')
    else:
        print(f'下载失败，状态码：{response.status_code}')