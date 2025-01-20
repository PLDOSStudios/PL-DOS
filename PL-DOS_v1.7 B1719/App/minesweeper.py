import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.mine_grid = [['0' for _ in range(width)] for _ in range(height)]
        self.revealed = [['0' for _ in range(width)] for _ in range(height)]
        self.plant_mines()
        self.fill_hints()

    def plant_mines(self):
        mines_planted = 0
        while mines_planted < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.mine_grid[y][x] != 'M':
                self.mine_grid[y][x] = 'M'
                mines_planted += 1

    def fill_hints(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.mine_grid[y][x] == 'M':
                    continue
                mines_around = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.mine_grid[ny][nx] == 'M':
                                mines_around += 1
                self.grid[y][x] = str(mines_around)

    def reveal(self, x, y):
        if self.revealed[y][x] == '1':
            return
        self.revealed[y][x] = '1'
        if self.grid[y][x] == '0':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)

    def print_grid(self):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                if self.revealed[y][x] == '1':
                    row += self.grid[y][x] + ' '
                else:
                    row += '. '
            print(row)

    def is_mine(self, x, y):
        return self.mine_grid[y][x] == 'M'

    def play(self):
        while True:
            self.print_grid()
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid coordinates. Try again.")
                    continue
                self.reveal(x, y)
                if self.is_mine(x, y):
                    print("[!] 你踩到雷了!")
                    self.print_grid()
                    print("Mine grid:")
                    for row in self.mine_grid:
                        print(''.join(row) + ' ')
                    break
            except ValueError:
                print("Invalid input. Please enter two integers.")

# Example usage
game = Minesweeper(10, 10, 10)
game.play()
