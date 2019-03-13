class Grid:
    def __init__(self, grid_string):
        self.x, self.y = self.parse_dimensions(grid_string)
        self.data = self.parse_data(grid_string)
        self.mined_grid = None

    def parse_dimensions(self, grid_string):
        x = grid_string[1]
        y = grid_string[3]
        return int(x), int(y)

    def parse_data(self, grid_string):
        data = grid_string[4:]
        if len(data) is not self.x * self.y:
            raise SyntaxError

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

        string_grid = ""
        for j in range(1, self.y + 1):
            for i in range(1, self.x + 1):
                string_grid += str(padded_grid[j][i])
            string_grid += "\n"
        return string_grid

    def __str__(self):
        return self.get_mines_surronding_squares()
