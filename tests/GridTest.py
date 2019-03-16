from unittest import TestCase, main

from src.Grid import Grid


class GridTest(TestCase):
    MAX_NUMBER_MINES_AROUND_SQUARE = 8
    MAX_NUMBER_MINES_CENTER_FOR_ROW = 3
    MAX_NUMBER_MINES_CORNER_FOR_ROW = 2

    def test_when_parsing_grid_then_correct_dimensions_are_set(self):
        string = "x1y1*"
        grid = Grid(string)

        self.assertEqual((grid.x, grid.y), (1, 1))

    def test_given_invalid_grid_data_when_parsing_then_raises(self):
        string = "x1y1.."
        with self.assertRaises(SyntaxError):
            grid = Grid(string)

    def test_when_parsing_grid_then_correct_data_is_set(self):
        grid_data = "*..*"
        string = "x2y2" + grid_data
        grid = Grid(string)

        self.assertEqual(len(grid_data), sum(len(x) for x in grid.data))

    def test_when_parsing_grid_then_column_number_matches_input(self):
        grid_data = "...***"
        string = "x3y2" + grid_data
        grid = Grid(string)

        self.assertEqual(3, len(grid.data[0]))

    def test_when_parsing_grid_then_row_number_matches_input(self):
        grid_data = "...***"
        string = "x3y2" + grid_data
        grid = Grid(string)

        self.assertEqual(2, len(grid.data))

    def test_when_adding_padding_then_it_is_correctly_set(self):
        string = "x2y3.*.*.*"
        grid = Grid(string)
        padded = grid.pad_grid(grid.data)

        self.assertEqual((3 + 2) * (2 + 2), sum(len(x) for x in padded))

    def test_when_checking_for_mines_then_detects_right_number(self):
        string = "x3y3****.****"
        middle = 4
        grid = Grid(string)
        mined_string = grid.get_mines_surronding_squares()
        mined_string = mined_string.replace('\n', '')

        self.assertEqual(self.MAX_NUMBER_MINES_AROUND_SQUARE, int(mined_string[middle]))

    def test_when_checking_for_mines_on_sides_then_detects_right_number(self):
        string = "x1y3.*."
        grid = Grid(string)
        mined_string = grid.get_mines_surronding_squares()
        mined_string = mined_string.replace('\n', '')

        self.assertEqual(int(mined_string[0]), 1)
        self.assertEqual(int(mined_string[2]), 1)

    def test_when_checking_for_mines_on_top_then_detects_right_number(self):
        string = "x3y2***..."
        grid = Grid(string)
        mined_string = grid.get_mines_surronding_squares()
        mined_string = mined_string.replace('\n', '')

        self.assertEqual(int(mined_string[4]), self.MAX_NUMBER_MINES_CENTER_FOR_ROW)
        self.assertEqual(int(mined_string[3]), self.MAX_NUMBER_MINES_CORNER_FOR_ROW)

    def test_when_checking_for_mine_on_bottom_then_detects_rigth_number(self):
        string = "x3y2...***"
        grid = Grid(string)

        mined_string = grid.get_mines_surronding_squares()
        mined_string = mined_string.replace('\n', '')

        self.assertEqual(int(mined_string[1]), self.MAX_NUMBER_MINES_CENTER_FOR_ROW)
        self.assertEqual(int(mined_string[0]), self.MAX_NUMBER_MINES_CORNER_FOR_ROW)


if __name__ == '__main__':
    main()
