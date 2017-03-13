
def is_threatened_square(positions, row, col):
    diag_1 = row + col
    diag_2 = row - col
    for pos_row, pos_col in positions:
        if pos_row + pos_col == diag_1 or \
            pos_row - pos_col == diag_2 or \
            row == pos_row or \
            col == pos_col:
            return True
    return False

def find_not_threatened_square(curr_queen_poss, n, positions):
    curr_row, curr_col = curr_queen_poss
    for col in range(curr_col, n):
        if not is_threatened_square(positions, curr_row, col):
            return (curr_row, col)
    return None

def _get_n_queen_positions(curr_row, n, positions):
    if curr_row > n-1:
        return True
    curr_col = -1
    while True:
        not_threatened_square = find_not_threatened_square((curr_row, curr_col+1), n, positions)
        if not_threatened_square:
            curr_col = not_threatened_square[1]
            positions.append(not_threatened_square)
            sub_problems_work = _get_n_queen_positions(curr_row + 1, n, positions)
            if sub_problems_work:
                return True
            else:
                positions.pop()
        else:
            return False

def get_n_queen_positions(num_queens):
    positions = []
    _get_n_queen_positions(0, num_queens, positions)
    return positions

def build_board_from_positions(positions, n):
    board = []
    for row, col in positions:
        board.append("." * (col) + 'Q' + '.' * (n-col-1))
    return board

class Solution(object):
    def solveNQueens(self, n):
        positions = get_n_queen_positions(n)
        board = build_board_from_positions(positions, n)
        return board

class TestNQueen(object):
    def test_theatened_square(self):
        assert is_threatened_square([(0,0)], 0, 0)
        assert is_threatened_square([(0,0)], 6, 6)
        assert is_threatened_square([(0,0)], 0, 6)
        assert is_threatened_square([(0,0)], 6, 0)
        assert is_threatened_square([(2,3)], 0, 1)

    def test_n_queen_problem(self):
        assert get_n_queen_positions(1) == [(0,0)]
        assert get_n_queen_positions(2) == []
        assert get_n_queen_positions(3) == []
        assert get_n_queen_positions(4) == [(0,1), (1,3), (2,0), (3,2)]

    def test_leetcode_solution(self):
        s = Solution()
        s.solveNQueens(4)