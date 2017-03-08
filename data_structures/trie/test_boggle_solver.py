from boggle_solver import BoggleSolver

class TestBogleSolver(object):
    def get_sample_boggle_board(self):
        return [
            "abcd",
            "efgh",
            "ijkl",
            "mnop"
        ]

    def test_is_valid_square(self):
        assert BoggleSolver.is_valid_position(self.get_sample_boggle_board(), 0, 0)
        assert BoggleSolver.is_valid_position(self.get_sample_boggle_board(), 2, 3)
        assert BoggleSolver.is_valid_position(self.get_sample_boggle_board(), 3, 3)
        assert not BoggleSolver.is_valid_position(self.get_sample_boggle_board(), 0, 4)
        assert not BoggleSolver.is_valid_position(self.get_sample_boggle_board(), 4, 0)
        assert not BoggleSolver.is_valid_position(self.get_sample_boggle_board(), 4, 4)

    def test_boggle_solver(self):
        bs = BoggleSolver()
        # bs.init_dictionary_from_list(['min', 'herp', 'nok', 'dgil'])
        bs.init_dictionary_from_file("dictionary.txt")
        bs.solve(self.get_sample_boggle_board())
