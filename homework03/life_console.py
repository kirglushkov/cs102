import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        for x in range(0, self.life.rows + 1):
            for y in range(0, self.life.cols + 1):
                if x in (0, self.life.rows):
                    if y not in (0, self.life.cols):
                        screen.addstr(x, y, "-")
                    else:
                        screen.addstr(x, y, "+")
                elif y in (0, self.life.cols):
                    screen.addstr(x, y, "|")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        screen.clear()
        for y in range(1, self.life.rows + 1):
            for x in range(1, self.life.cols + 1):
                if not self.life.curr_generation[y - 1][x - 1]:
                    screen.addstr(y, x, " ")
                else:
                    screen.addstr(y, x, "*")

    def run(self) -> None:
        window = curses.initscr()
        game_running = True
        while game_running:
            self.draw_grid(window)
            self.draw_borders(window)
            self.life.step()
            window.refresh()
            curses.napms(150)
        curses.endwin()


if __name__ == "__main__":
    life = GameOfLife((24, 80), max_generations=100)
    ui = Console(life)
    ui.run()
