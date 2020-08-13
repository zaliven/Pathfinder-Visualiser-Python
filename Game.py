from spot import Spot, WHITE, GRAY
from queue import PriorityQueue


class Game:
    def __init__(self, pygame, win, width, rows, algorithmChoice):
        self.pygame = pygame
        self.win = win
        self.width = width
        self.rows = rows
        self.grid = []
        self.make_grid()
        self.start = None
        self.end = None
        self.use_heuristic = True
        self.use_distance = True
        self.algorithmChoice = algorithmChoice

        if algorithmChoice == 'dijkstra':
            self.use_heuristic = False
        if algorithmChoice == 'gbf':
            self.use_distance = False
        self.algorithm = self.pathfind

    @staticmethod
    def h(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, current):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            self.draw()

    def pathfind(self):
        count = 0
        heuristic = 0
        open_set = PriorityQueue()
        open_set.put((0, count, self.start))
        came_from = {}
        h_score = {spot: float("inf") for row in self.grid for spot in row}
        h_score[self.start] = 0
        g_score = {spot: float("inf") for row in self.grid for spot in row}
        g_score[self.start] = 0
        f_score = {spot: float("inf") for row in self.grid for spot in row}
        f_score[self.start] = self.h(self.start.get_pos(), self.end.get_pos())

        open_set_hash = {self.start}

        while not open_set.empty():
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == self.end:
                self.reconstruct_path(came_from, self.end)
                self.end.make_end()
                self.start.make_start()
                return True

            for neighbor in current.neighbors:
                if self.use_distance:
                    temp_g_score = g_score[current] + 1
                    if temp_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = temp_g_score
                        if self.use_heuristic:
                            heuristic = self.h(neighbor.get_pos(), self.end.get_pos())
                        f_score[neighbor] = temp_g_score + heuristic
                        if neighbor not in open_set_hash:
                            count += 1
                            open_set.put((f_score[neighbor], count, neighbor))
                            open_set_hash.add(neighbor)
                            neighbor.make_open()

                if not self.use_distance:
                    temp_h_score = self.h(neighbor.get_pos(), self.end.get_pos()) + 1
                    if temp_h_score < h_score[neighbor]:
                        came_from[neighbor] = current
                        h_score[neighbor] = temp_h_score
                        if neighbor not in open_set_hash:
                            count += 1
                            open_set.put((h_score[neighbor], count, neighbor))
                            open_set_hash.add(neighbor)
                            neighbor.make_open()
            self.draw()

            if current != self.start:
                current.make_closed()
        return False

    def make_grid(self):
        self.grid = []
        gap = self.width // self.rows
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                spot = Spot(i, j, gap, self.rows, self.pygame)
                self.grid[i].append(spot)

    def draw_grid(self):
        gap = self.width // self.rows
        for i in range(self.rows):
            self.pygame.draw.line(self.win, GRAY, (0, i * gap), (self.width, i * gap))
            for j in range(self.rows):
                self.pygame.draw.line(self.win, GRAY, (j * gap, 0), (j * gap, self.width))

    def draw(self):
        self.win.fill(WHITE)
        for row in self.grid:
            for spot in row:
                spot.draw(self.win)
        self.draw_grid()
        self.pygame.display.update()

    def get_clicked_pos(self, pos):
        gap = self.width // self.rows
        y, x = pos
        row = y // gap
        col = x // gap
        return row, col
