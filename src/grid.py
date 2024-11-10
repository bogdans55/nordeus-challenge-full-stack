import pygame
import random
from src.api import fetch_grid_data

class Grid:
    def __init__(self, screen, rows=30, cols=30, cell_size=20):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = self.load_grid()

    def load_grid(self):
        """Loads the grid data from the API. If the API call fails, generate a random grid."""
        try:
            grid = fetch_grid_data()
            print("Successfully fetched grid data from API.")
            return grid
        except Exception as e:
            print("Falling back to generating a random grid.")
            return self.generate_random_grid()

    def generate_random_grid(self):
        """Generates a random grid with some islands and water."""
        grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                if row > 0 and grid[row-1][col] != 0 and random.random() < 0.3:
                    grid[row][col] = random.randint(max(1, grid[row-1][col] - 100), min(1000, grid[row-1][col] + 100))
                elif col > 0 and grid[row][col-1] != 0 and random.random() < 0.3:
                    grid[row][col] = random.randint(max(1, grid[row-1][col] - 100), min(1000, grid[row-1][col] + 100))
                elif random.random() < 0.8:
                    grid[row][col] = 0               
                else:
                    grid[row][col] = random.randint(1, 1000)
        return grid
    
    def draw(self, incorrect_guesses=None):
        """Draws the grid on the screen with colors based on cell heights."""
        for row in range(self.rows):
            for col in range(self.cols):
                height = self.grid[row][col]
                color = self.get_color_for_height(height)
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                )
                
                for island in incorrect_guesses:
                    if (row, col) in island:
                        red_tint = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
                        red_tint.fill((255, 0, 0, 100))
                        self.screen.blit(red_tint, (col * self.cell_size, row * self.cell_size))


    
    def get_color_for_height(self, height):
        """Returns a color based on height. Water (0) is blue; land varies by height."""
        if height == 0:
            return (0, 100, 255)
        else:
            if height < 400:
                return (0, int(255 * (height / 400)), 0)
            elif height < 700:
                return (int(255 * ((height - 400) / 300)), 255, 0)
            elif height < 900:
                return (109, int(69 + (186 * ((height - 700) / 200))), 19)
            else:
                return (int(255 - (1000 - height) / 5), int(255 - (1000 - height) / 5), int(255 - (1000 - height) / 5))

    def get_island(self, x, y):
        """Gets the island based on a cell click at (x, y). Returns the list of cells that make up the island."""
        row, col = y // self.cell_size, x // self.cell_size
        if self.grid[row][col] == 0:
            return None
        return self.find_island_cells(row, col)

    def find_island_cells(self, row, col, visited=None):
        """Finds all cells in the connected land area (island) starting from (row, col)."""
        if visited is None:
            visited = set()
        if (row, col) in visited or not (0 <= row < self.rows) or not (0 <= col < self.cols) or self.grid[row][col] == 0:
            return visited

        visited.add((row, col))
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.find_island_cells(row + dr, col + dc, visited)
        return visited

    def calculate_average_height(self, island):
        """Calculates the average height of the specified cells (island)."""
        if not island:
            return 0
        return sum(self.grid[row][col] for row, col in island) / len(island)

    def find_highest_average_island(self):
        """Finds the island with the highest average height."""
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        max_avg_height = 0
        target_island = set()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != 0 and not visited[row][col]:
                    island = self.find_island_cells(row, col)
                    for r, c in island:
                        visited[r][c] = True
                    avg_height = self.calculate_average_height(island)
                    if avg_height > max_avg_height:
                        max_avg_height = avg_height
                        target_island = island
        return target_island

