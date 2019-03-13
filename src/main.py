from src.Grid import Grid

grid_input = "x1y1*"

grid_input = "x2y2****"
# grid_input = "x2y1**"
# grid_input = "x1y1*"
grid_input = "x3y1.**"
grid_input = "x4y4.*.***.*********"
#
grid = Grid(grid_input)

grid.set_number_of_mines()

print(grid)





