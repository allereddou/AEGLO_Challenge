from src.Grid import Grid

try:
    lines = [line.rstrip('\n') for line in open('minesweeper.txt')]
except FileNotFoundError:
    raise IOError("File 'minesweeper.txt' needs to exist !")

for line in lines:
    grid = Grid(line)
    print(grid)
