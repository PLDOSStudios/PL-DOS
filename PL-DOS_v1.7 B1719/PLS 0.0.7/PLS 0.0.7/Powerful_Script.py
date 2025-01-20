import importlib
import random
print("welcome to powerful script")

def run(code):
    global l
    voids = []
    varss = {}
    lists = {}
    loops = {}
    loop_stack = []

    def void(dd):
        voids.append([dd, l, 0])

    def enter(a):
        eee = input()
        varss.update({a: eee})

    def intt(ew):
        varss[ew] = int(varss[ew])

    def strr(ew):
        varss[ew] = str(varss[ew])

    def listt(ew):
        lists[ew] = []

    def add(list_name, *values):
        if list_name not in lists:
            lists[list_name] = []
        for value in values:
            try:
                value = int(value)
            except:
                pass
            lists[list_name].append(value)

    def loop(times, label):
        if int(times) >= 0:
            try:
                loops[label] = int(times)
            except ValueError:
                loops[label] = varss[times]
        elif int(times) == -1:
            loops[label] = int(9999999999999999999)

    def endloop(label):
        if loops[label] > 1:
            loops[label] -= 1
            return True
        else:
            return False  # Indicate that the loop should end
    def change(a, b):
        varss[a] = b

    def swap(a, b, c):
        lists[a][c], lists[a][b] = lists[a][b], lists[a][c]

    def var(a, b):
        varss.update({a: b})

    def plus(a, b):
        varss[a] += int(b)

    def getindex(a, b):
        index = int(b)
        return lists[a][index]

    def getlistindex(a, b):
        return lists[a][int(b)]

    def floatt(a):
        varss[a] = float(varss[a])

    def pack(a):
        if a == 'main':
            return
        elif a == 'autosave':
            with open('autosave.plsc', 'w') as f:
                f.write(code)

    def if_statement(a, b, c):
        if eval(a):
            exec(c)

    def r(a, b, c):
        varss[c] = random.randint(int(a), int(b))

    def break_loop(label):
        if label in loops:
            loops[label] = 0
            return
        else:
            print(f"循环 {label} 不存在。")

    commands = {
        'printd': lambda x: print(int(x)),
        'print': lambda x: print(x),
        'printv': lambda x: print(varss[x]),
        'out': lambda x: print(x, end=''),
        'prints': lambda x: print(str(x)),
        'printl': lambda x: print(lists[x]),
        'package' : lambda x: pack(x),
        'end': lambda: 'exit',
        'void': lambda dd: void(dd),
        'getindex':lambda a, b:getindex(a, b),
        'getlistindex': lambda a, b: getlistindex(a, b),
        'enter': lambda a: enter(a),
        'int': lambda a: intt(a),
        'swap': lambda a, b, c: swap(a, b, c),
        'plus': lambda a, b: plus(a, b),
        'str': lambda a: strr(a),
        'float' : lambda a: floatt(a),
        'change': lambda a, b: change(a, b),
        'list': lambda a: listt(a),
        'var': lambda a, b: var(a, b),
        'add': lambda list_name, *values: add(list_name, *values),
        'remove': lambda list_name, item: lists[list_name].remove(item),
        'loop': lambda times, label: loop(times, label),
        'endloop': lambda label: endloop(label),
        'randi' : lambda a, b, c: r(a, b, c),
        'if' : lambda a, b, c: if_statement(a, b, c),
        'endif':lambda: None,
        'break': lambda label: break_loop(label),  # 新增：中断循环的命令
    }

    lines = code.splitlines()
    line_index = 0
    while line_index < len(lines):
        line = lines[line_index].strip()
        if not line:
            line_index += 1
            continue
        if loop_stack and line.startswith('endloop'):
            _, label = line.split()
            if loops[label] > 1:
                loops[label] -= 1
                line_index = loop_stack[-1]  # Reset to the start of the loop
            else:
                loop_stack.pop()  # Remove loop from stack
                line_index += 1  # Move to the next line after the loop
            continue
        elif line.startswith('loop'):
            _, times, label = line.split()
            commands['loop'](times, label)
            loop_stack.append(line_index)  # Remember the start of the loop
        else:
            command, *args = line.split()
            if command in commands:
                if command == 'break':  # 特殊处理break命令
                    commands[command](*args)
                    if loop_stack:  # 如果有循环在运行，则跳转到循环的末尾
                        loop_stack.pop()  # 移除当前循环的起始索引
                        continue
                else:
                    commands[command](*args)
            else:
                print(f"未知命令: {command}")

def save_code_to_file(code, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(code))

import os

# ... (其他代码保持不变)

def import_module(module_name):
    # Construct the path to the module file
    module_file = os.path.join('mods', f'{module_name}.plsc')
    # Check if the file exists
    if not os.path.isfile(module_file):
        print(f"模块 {module_name} 不存在。")
        return
    # Read the content of the module file
    with open(module_file, 'r') as file:
        module_code = file.read()
    # Run the module code
    run(module_code)

def main():
    print('Powerful Script 0.0.7')
    code = []
    if_block = False
    if_condition = ""
    if_body = []

    while True:
        cod = input(">>> ")
        if cod.lower().strip() == "exit":
            print("退出程序")
            break
        elif cod.lower().startswith("if"):
            if_block = True
            if_condition = cod[3:].strip()
            continue
        elif cod.lower().strip() == "endif":
            if_body.append(cod)  # 将 endif 加入到 if 语句体中
            code.extend(["if " + if_condition] + if_body)
            if_block = False
            if_body = []
            continue
        elif if_block:
            if_body.append(cod)
            continue

        code.append(cod)
        if cod.strip() == "end":
            result = run("\n".join(code))
            if result == 'exit':
                break
            code = []

if __name__ == '__main__':
    main()