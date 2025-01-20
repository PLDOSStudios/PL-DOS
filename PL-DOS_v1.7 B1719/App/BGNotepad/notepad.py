import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

class Notepad(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.filename = None
        self.pack()
        self.create_widget()

    def create_widget(self):
        menu = tk.Menu(self.master)

        menu_file = tk.Menu(menu, tearoff=0)
        menu_edit = tk.Menu(menu, tearoff=0)
        menu_help = tk.Menu(menu, tearoff=0)
        menu_guanyu = tk.Menu(menu, tearoff=0)

        menu.add_cascade(label='文件', menu=menu_file)
        menu.add_cascade(label='编辑', menu=menu_edit)
        menu.add_cascade(label='帮助', menu=menu_help)
        menu.add_cascade(label='关于', menu=menu_guanyu)

        menu_file.add_command(label='新建', accelerator='Ctrl+N', command=self.new)
        menu_file.add_command(label='打开', accelerator='Ctrl+O', command=self.open)
        menu_file.add_command(label='保存', accelerator='Ctrl+S', command=self.save)
        menu_file.add_separator()
        menu_file.add_command(label='退出', accelerator='Ctrl+Q', command=self.exit)

        menu_guanyu.add_command(label='关于', command=self.about)

        self.textpad = tk.Text(self.master, width=100, height=70, font=('Microsoft YaHei', 10))
        self.textpad.pack(fill=tk.BOTH, expand=True)

        self.context_menu = tk.Menu(self.textpad, tearoff=0)
        self.context_menu.add_command(label='背景颜色', command=self.change_bg_color)

        self.master.config(menu=menu)

        self.frame = tk.Frame(self.master, height=20, bg='#D4D4D4')
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.kkb = tk.Label(self.master, text='字符数 0', bg='#D4D4D4')
        self.kkb.place(x=10, y=640)

        self.scr = tk.Scrollbar(self.textpad)
        self.scr.pack(side=tk.RIGHT, fill=tk.Y)
        self.textpad.config(yscrollcommand=self.scr.set)
        self.scr.config(command=self.textpad.yview)

        self.master.bind("<Button-3>", self.create_context_menu)

        self.update_kb()

    def open(self):
        self.filename = filedialog.askopenfilename(title='打开文件')
        if self.filename:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.textpad.delete(1.0, tk.END)
                self.textpad.insert(1.0, file.read())

    def about(self):
        messagebox.showinfo(title='关于', message='作者：BG-DOS开发者团队')

    def save(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(title='保存文件', defaultextension=".txt")
        if self.filename:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(self.textpad.get(1.0, tk.END))

    def exit(self):
        self.master.quit()

    def new(self):
        self.filename = None
        self.textpad.delete(1.0, tk.END)

    def change_bg_color(self):
        color_code = colorchooser.askcolor(title="选择背景颜色")[1]
        if color_code:
            self.textpad.config(bg=color_code)

    def update_kb(self):
        self.kkb.config(text=f'字符数 {len(self.textpad.get("1.0", tk.END)) - 1}')
        self.master.after(40, self.update_kb)

    def create_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x660")
    root.title('BGNotePad')
    notepad = Notepad(master=root)
    root.mainloop()
