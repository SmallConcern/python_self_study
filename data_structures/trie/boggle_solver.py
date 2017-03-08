from trie import Trie

class BoggleSolver(object):
    def __init__(self):
        self.trie = Trie()
        self.NEIGHBOR = [(-1, -1), (-1, 0), (-1, 1),
                         ( 0, -1),          ( 0, 1),
                         ( 1, -1), ( 1, 0), ( 1, 1)]

    @staticmethod
    def is_valid_position(board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

    def init_dictionary_from_file(self, dict_file):
        with open(dict_file, 'r') as dict:
            for word in dict.readlines():
                if len(word) > 2:
                    self.trie.add_word(word.lower().replace('\n', ''))

    def init_dictionary_from_list(self, dict_list):
        for word in dict_list:
            self.trie.add_word(word)

    def _recursive_boggle_solve(self, board, row, col, path, char_buff):
        if self.trie.is_word(char_buff):
            print(char_buff)
        for delta_row, delta_column in self.NEIGHBOR:
            new_row = row + delta_row
            new_col = col + delta_column
            if (new_row, new_col) not in path and \
                    BoggleSolver.is_valid_position(board, new_row, new_col):
                if self.trie.is_prefix(char_buff + board[new_row][new_col]):
                    path.append((new_row, new_col))
                    self._recursive_boggle_solve(board, new_row, new_col, path, char_buff + board[new_row][new_col])
                    del path[-1]

    def solve(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                self._recursive_boggle_solve(board, row, col, [(row,col)], board[row][col])


