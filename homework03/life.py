import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]






class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if not randomize:
            return [[0 for _ in range(self.cols)] for __ in range(self.rows)]
        else:
            return [[random.choice([0, 1]) for _ in range(self.cols)] for __ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        nbours = []
        x, y = cell[0], cell[1]

        if x - 1 >= 0:
            if y - 1 >= 0:
                nbours.append(self.curr_generation[x - 1][y - 1])
            nbours.append(self.curr_generation[x - 1][y])
            if self.cols > y + 1:
                nbours.append(self.curr_generation[x - 1][y + 1])
        if 0 <= y - 1:
            nbours.append(self.curr_generation[x][y - 1])
        if self.cols > y + 1:
            nbours.append(self.curr_generation[x][y + 1])
        if self.rows > x + 1:
            if 0 <= y - 1:
                nbours.append(self.curr_generation[x + 1][y - 1])
            nbours.append(self.curr_generation[x + 1][y])
            if self.cols > y + 1:
                nbours.append(self.curr_generation[x + 1][y + 1])
        return nbours

    def get_next_generation(self) -> Grid:
        grid = self.create_grid()

        for row in range(self.rows):
            for col in range(self.cols):
                cell = (row, col)
                sum_of_neighb = sum(self.get_neighbours(cell))
                if not (not (sum_of_neighb < 2) and not (sum_of_neighb > 3)):
                    grid[row][col] = 0
                elif not sum_of_neighb != 3:
                    grid[row][col] = 1
        return grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        pass

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        pass

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
