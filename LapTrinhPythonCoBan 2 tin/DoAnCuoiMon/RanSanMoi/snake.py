import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Độ lớn của game
width = 500
height = 500

# Cột và hàng (grid)
cols = 25
rows = 20

# Ô vuông cho rắn, thức ăn, bàn cờ game
class cube():
    rows = 20
    w = 500

    def __init__(self, start, dirnx=0, dirny=0, color=(255, 0, 0)):
        self.pos = start  # Tọa độ hiện tại trên lưới
        self.dirnx = dirnx  # Hướng di chuyển trục X (-1: Trái, 1: Phải)
        self.dirny = dirny  # Hướng di chuyển trục Y (-1: Lên, 1: Xuống)
        self.color = color  # Màu sắc của khối

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        # Dùng để bắt sự kiện rắn đụng tường
        # self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

        # Dùng % rows để rắn đi qua tường mà không mất thân
        self.pos = (
            (self.pos[0] + self.dirnx) % self.rows,
            (self.pos[1] + self.dirny) % self.rows
        )

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        # Vẽ hình chữ nhật đại diện cho khối
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        # Nếu là đầu rắn (eyes=True) thì khối mới đó sẽ có mắt
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

# Tạo ra con rắn
class snake():
    body = []  # thân rắn (cube màu khác)
    turns = {}  # Lưu trữ hướng rẽ của rắn tại các tọa độ

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # Khởi tạo đầu rắn
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        # out game khi thoát
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Lấy trạng thái của các phím bấm
        keys = pygame.key.get_pressed()

        # Bắt sự kiện để thực hiện rẽ rắn
        if keys[pygame.K_LEFT]:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_RIGHT]:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_UP]:
            self.dirny = -1
            self.dirnx = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_DOWN]:
            self.dirny = 1
            self.dirnx = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Cho từng khúc của rắn di chuyển theo vết rẽ hoặc hướng hiện tại
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)  # Xóa góc cua khi khúc cuối cùng đã đi qua
            else:
                c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        # Đặt lại trạng thái khi rắn chết
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        # +1 thân khi đc ăn
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # Khúc đầu tiên vẽ thêm mắt
            else:
                c.draw(surface)  # Các khúc thân phía sau vẽ bình thường


# Hàm vẽ lại toàn bộ giao diện game mỗi khung hình
def redrawWindow():
    global win
    win.fill((0, 0, 0))  # Xóa màn hình = vc phủ màu đen
    drawGrid(width, rows, win)  # Vẽ lưới bàn cờ
    s.draw(win)  # Vẽ con rắn
    snack.draw(win)  # Vẽ mồi
    pygame.display.update()  # Cập nhật hiển thị lên cửa sổ
    pass


# Hàm vẽ các đường lưới chia ô vuông trên màn hình
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


# Tạo đồ ăn (đảm bảo không đè lên thân rắn)
def randomSnack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(1, rows - 1)
        y = random.randrange(1, rows - 1)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)

# Hàm chính điều khiển luồng trò chơi
def main():
    global s, snack, win
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))  # Khởi tạo rắn màu đỏ tại tọa độ (10, 10)
    s.addCube()
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))  # Khởi tạo mồi màu xanh lá
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)  # Giới hạn tốc độ game ở 10 khung hình/giây
        s.move()
        headPos = s.head.pos


        # 1.1. Chế độ đụng tường là chết (code dòng 30)
        if headPos[0] >= rows or headPos[0] < 0 or headPos[1] >= rows or headPos[1] < 0:
            print("Score:", len(s.body))
            s.reset((10, 10))

        # 1.2. Chế độ đi qua tường (code 32-35)

        # 2. Kiểm tra nếu đầu rắn ăn được mồi -> Tăng chiều dài và sinh mồi mới
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        # 3. Kiểm tra nếu đầu rắn tự cắn vào thân mình -> Thua, reset game
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print("Score:", len(s.body))
                s.reset((10, 10))
                break
        redrawWindow()

# Chạy hàm main để khởi động game
main()