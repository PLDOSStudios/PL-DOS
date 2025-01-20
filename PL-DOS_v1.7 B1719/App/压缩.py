import zipfile
import os


def zip_folder():
    folder_path = input("请输入要压缩的文件夹路径: ")
    save_path = input("请输入压缩文件保存的路径（包括文件名，例如：/home/user/output.zip）: ")
    with zipfile.ZipFile(save_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path)


if __name__ == "__main__":
    zip_folder()