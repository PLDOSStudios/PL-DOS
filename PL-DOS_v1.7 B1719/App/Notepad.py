import os


def write_to_file(filename, content, content_path):
    try:
        with open(content_path, 'w') as file:
            file.write(content)
        print(f"文件已保存为 {filename}")
    except IOError as e:
        print(f"保存文件时出错: {e}")

def open_file(path):
    try:
        with open(path, 'r') as file:
            ff = file.readlines()
            for i in ff:
                print(i)
            print('---------------------------')
            print('如果想更改内容请用save保存')
    except IOError as e:
        print(f'读取文件时出错: {e}')
def main():
    print("欢迎使用由BG-DOS团队制作的记事本")
    with open(r'System/Temp/now_user.txt', 'r') as file:
        nowuser = file.read()

    f = ''
    while True:
        line = input("请输入内容（‌输入 'save' 保存，‌输入 'exit' 退出，输入 'open' 打开）‌：‌")
        if line.lower() == 'save':
            filename = input("请输入要保存的文件名（‌.bgusernote将被自动添加）‌：‌")
            if not filename.endswith('.bgusernote'):
                filename += '.bgusernote'
            content_path = fr"Users/{nowuser}/Note/{filename}"
            write_to_file(filename, f, content_path)
            f = ""
        elif line.lower() == 'exit':
            print("退出写字板。‌")
            break
        elif line.lower() == 'open':
            dir_path = fr'Users/{nowuser}/Note/'
            for item in os.listdir(dir_path):
                full_path = os.path.join(dir_path, item)
                if os.path.isfile(full_path):
                    pass
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    print(os.path.join(file))
            a = input('请输入文件名')
            if not a.endswith('.TXT'):
                a += '.TXT'
            content_path = fr"Users/{nowuser}/Note/{a}"
            open_file(content_path)
        else:
            f += line + "\n"

if __name__ == "__main__":
    main()
