import re

class Grid:
    def __init__(self, grid_string):
        self.x, self.y = self.parse_dimensions(grid_string)
        self.data = self.parse_data(grid_string)

    def parse_dimensions(self, grid_string):
        pos = re.findall(r'(\D+)(\d+)', grid_string)
        x = pos[0][1]
        y = pos[1][1]
        return int(x), int(y)

    def parse_data(self, grid_string):
        if self.x is not self.y:
            data = grid_string.split(str(self.x))[1].split(str(self.y))[1]
        else:
            data = grid_string.split(str(self.x))[2]

        if len(data) is not self.x * self.y:
            raise SyntaxError("File contains a mistake and thus is unparsable")

        output = [[data[self.x * i + j] if data[self.x * i + j] is not '.' else 0 for j in range(self.x)] for i in
                  range(self.y)]
        return output

    def pad_grid(self, grid):
        for j in range(self.y):
            grid[j] = [0] + grid[j] + [0]
        grid.append([0 for i in range(self.x + 2)])
        grid.insert(0, [0 for i in range(self.x + 2)])
        return grid

    def get_mines_surronding_squares(self):
        padded_grid = self.pad_grid(self.data)

        for j in range(1, self.y + 1):
            for i in range(1, self.x + 1):
                if padded_grid[j][i] is "*":
                    # increment top
                    for k in range(-1, 2):
                        if padded_grid[j - 1][i + k] is not "*":
                            padded_grid[j - 1][i + k] += 1

                    # increment sides
                    for k in range(-1, 2, 2):
                        if padded_grid[j][i + k] is not "*":
                            padded_grid[j][i + k] += 1

                    # increment bottom
                    for k in range(-1, 2):
                        if padded_grid[j + 1][i + k] is not "*":
                            padded_grid[j + 1][i + k] += 1

        mined_grid = ""
        for j in range(1, self.y + 1):
            for i in range(1, self.x + 1):
                mined_grid += str(padded_grid[j][i])
            mined_grid += "\n"
        return mined_grid

    def __str__(self):
        return self.get_mines_surronding_squares()
