import zipfile

def unzip_file(zip_file_path, extract_to):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"文件已成功解压到 {extract_to}")
    except zipfile.BadZipFile:
        print("无效的ZIP文件，请检查文件是否损坏。")
    except FileNotFoundError:
        print("指定的ZIP文件不存在，请检查文件路径。")


if __name__ == "__main__":
    zip_file_path = input("请输入ZIP文件的路径: ")
    extract_to ="解压"
    unzip_file(zip_file_path, extract_to)