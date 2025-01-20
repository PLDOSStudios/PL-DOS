from tkinter import *
from tkinter import messagebox, filedialog
import os
import hashlib
import tkinter as tk
try:
    from PIL import Image, ImageTk
    import psutil
except:
    os.system("pip install pillow")
    os.system("pip install psutil"
    )

class CustomTitleBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.title_label = tk.Label(self, text="BG-DOS 杀毒软件", bg="skyblue", relief="raised", anchor="center")
        self.title_label.pack(fill="both", expand=True)
        self.close_button = tk.Button(self, text="✕", command=self.parent.destroy, bg="skyblue", fg="black", borderwidth=0, highlightthickness=0,)
        self.close_button.place(x = 880, y = 0)

        self.title_label.bind("<B1-Motion>", self.move_window)

    def move_window(self, event):
        self.parent.geometry(f"+{event.x_root}+{event.y_root}")

    def minimize_window(self):
        self.parent.iconify()

def start_scan():
    global aaa
    f = var.get()
    a = 0
    if not os.path.exists(f):
        messagebox.showerror('错误', '文件不存在')
        return
    for i in range(1):
        with open(f, 'rb') as f2:
            data = f2.read()
        md5 = hashlib.md5(data).hexdigest()
        print(md5)
        if md5 in aaa:
            messagebox.showwarning('卧槽', f'发现非常非常危险的文件：{f}')
            a += 1
            break
    if a == 0:
        messagebox.showinfo('敢不敢跟我比划比划', '没有发现任何病毒')


def dele(path_list):
    for path in path_list:
        try:
            os.remove(path)
            print(f"Deleted file: {path}")
        except OSError as e:
            print(f"Error deleting file {path}: {e}")


# 定义扫描函数
def normal_scan():
    global wf, aaa
    danger_files = []
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        files = os.listdir(folder_selected)
        real_files = [f for f in files if os.path.isfile(os.path.join(folder_selected, f))]

        print("Files in the selected folder:")
        danger_count = 0
        for file in real_files:
            file_path = os.path.join(folder_selected, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                md5 = hashlib.md5(data).hexdigest()
            if md5 in aaa:
                danger_count += 1
                danger_files.append(file_path)
                print(file_path)
        wf.config(text=f'共发现{danger_count}个病毒')
        if danger_count > 0:
            print(f"Number of dangerous files: {danger_count}")
            de.config(command=lambda: dele(danger_files))
        else:
            de.config(state=tk.DISABLED)

def browse_file():
    filename = filedialog.askopenfilename(
        title="选择文件",
        filetypes=(("应用程序", "*.exe"), ("PYMM文件", "*.pymm"), ("所有文件", "*.*"))
    )
    var.set(filename)

def home():
    global z
    b8.place(x = 60, y = 135)
    z = 1

def task():
    import psutil
    pids = psutil.pids()
    processes = [psutil.Process(pid) for pid in pids]
    for process in processes:
        pass
    root.after(1100, task)

def co():
    global z
    b8.place(x = 60, y = 185)
    z = 2

def tools():
    global z
    b8.place(x = 60, y = 235)
    z = 3

def loop():
    global a, e, f
    if z == 1:
        a.place(x = 190, y = 40)
        e.place(x = 700, y = 40)
        f.place(x = 130, y = 40)
        fffff.place(x = 5, y = 690)
        dd.place(x=760, y=40)
        ff.place_forget()
        fff.place_forget()
        eed.place_forget()
        tt.place_forget()
        de.place_forget()
        wf.place_forget()
    elif z == 2:
        a.place_forget()
        e.place_forget()
        f.place_forget()
        ff.place(x = 130, y = 44)
        fff.place(x=130, y=105)
        tt.place_forget()
        fffff.place(x=5, y=690)
        dd.place_forget()
        wf.place_forget()
        eed.place_forget()
        de.place_forget()
    elif z == 3:
        eed.place(x = 120, y = 150)
        a.place_forget()
        e.place_forget()
        f.place_forget()
        ff.place_forget()
        fff.place_forget()
        tt.place(x=130, y=44)
        de.place(x = 450, y = 110)
        dd.place_forget()
        fffff.place(x=5, y=690)
        wf.place(x = 120, y = 110)

    root.after(60, loop)

root = Tk()
root.geometry('900x730')
root.maxsize(900, 730)
root.minsize(900, 730)
root.overrideredirect(True)
root.title("BG-DOS杀毒软件")
root.configure(bg='white')

title_bar = CustomTitleBar(root, bg="skyblue")
title_bar.pack(fill="x")

z = 1
aaa = []

with open('病毒库.txt', 'r', encoding='utf-8') as file:
    for line in file:
        aaa.append(line.strip())

var = StringVar()
var.set('请输入文件路径')
a = Entry(root, textvariable=var, width=70)
a.place(x = 190, y = 40)

e = Button(root, text='开始扫描', command=start_scan)
e.place(x = 880, y = 0)

eed = Button(root, text = '普通扫描(md5)', command = normal_scan)

dd = Button(root, text='浏览', command=browse_file)
dd.place(x = 760, y = 0)

f = tk.Label(root, text='快速扫描', bg='white')

fffff = tk.Label(root, text='BG系列开发团队\n版权所有2024', bg='white', fg = 'gray')

ff = tk.Label(root, text='关于', font=('微软雅黑', 23), bg='white')

tt = tk.Label(root, text='病毒查杀', font=('微软雅黑', 23), bg='white')

fff = tk.Label(root, text='  BG-DOS杀毒软件\n 版权所有© 2024 \n BG-DOS 及 BG系列的所有团队', font=('微软雅黑', 14), bg='white')

image12 = r"Resources\logo.png"
im12 = Image.open(image12)
imp12 = ImageTk.PhotoImage(im12)

wf = tk.Label(root, text = '共发现0个病毒', font = ('微软雅黑', 20))

c = tk.Canvas(root, width=5, height=900, bg='black').place(x = 92, y = 21)

image = r"Resources\home.png"
im = Image.open(image)
imp = ImageTk.PhotoImage(im)

b1 = tk.Button(root, image=imp, compound='center', borderwidth=0, highlightthickness=0, command = home)
b1.pack()
b1.image = imp
b1.place(x = 0, y = 130)

b12 = tk.Button(root, image=imp12, compound='center', borderwidth=0, highlightthickness=0, command = lambda : messagebox.showinfo('滚', '恭喜你找到了彩蛋'))
b12.image = imp12
b12.place(x = 10, y = 25)

de = tk.Button(root, text = '立即删除')

image3 = r"Resources\virus.png"
im3 = Image.open(image3)
imp3 = ImageTk.PhotoImage(im3)

b3 = tk.Button(root, image=imp3, compound='center', borderwidth=0, highlightthickness=0, command = co)
b3.image = imp3
b3.place(x = 0, y = 180)

image6 = r"Resources\tools.png"
im6 = Image.open(image6)
imp6 = ImageTk.PhotoImage(im6)

b6 = tk.Button(root, image=imp6, compound='center', borderwidth=0, highlightthickness=0, command = tools)
b6.image = imp6
b6.place(x = 0, y = 230)

image8 = r"Resources\状态.png"
im8 = Image.open(image8)
imp8 = ImageTk.PhotoImage(im8)

b8 = tk.Button(root, image=imp8, compound='center', borderwidth=0, highlightthickness=0)
b8.image = imp8
b8.place(x = 60, y = 135)

loop()

root.mainloop()
