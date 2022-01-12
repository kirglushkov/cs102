import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (0, y), (self.width, y)
            )

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        if not randomize:
            return [[0 for _ in range(self.cols)] for __ in range(self.rows)]
        else:
            return [
                [random.choice([0, 1]) for _ in range(self.cols)]
                for __ in range(self.rows)
            ]

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for xheight in range(self.cell_height):
            for ywidth in range(self.cell_width):
                rect = pygame.Rect(
                    self.cell_size * ywidth,
                    self.cell_size * xheight,
                    self.cell_size,
                    self.cell_size,
                )
                if not self.grid[xheight][ywidth]:
                    pygame.draw.rect(self.screen, pygame.Color("red"), rect)
                else:
                    pygame.draw.rect(self.screen, pygame.Color("green"), rect)

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        cells = []
        x = cell[0] // self.cell_size
        y = cell[1] // self.cell_size
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.grid[x - 1][y - 1])
            cells.append(self.grid[x - 1][y])
            if self.cell_width > y + 1:
                cells.append(self.grid[x - 1][y + 1])
        if y - 1 >= 0:
            cells.append(self.grid[x][y - 1])
        if self.cell_width > y + 1:
            cells.append(self.grid[x][y + 1])
        if self.cell_height > x + 1:
            if y - 1 >= 0:
                cells.append(self.grid[x + 1][y - 1])
            cells.append(self.grid[x + 1][y])
            if self.cell_width > y + 1:
                cells.append(self.grid[x + 1][y + 1])
        return cells

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = []
        for y in range(0, self.height, self.cell_size):
            row = []
            for x in range(0, self.width, self.cell_size):
                if 3 == sum(self.get_neighbours((y, x))):
                    row.append(1)
                else:
                    if (
                        self.grid[y // self.cell_size][x // self.cell_size] != 1
                        or sum(self.get_neighbours((y, x))) != 2
                    ):
                        row.append(0)
                    else:
                        row.append(1)
            new_grid.append(row)
        self.grid = new_grid
        return self.grid
