
class PotsOfGold(object):
    @staticmethod
    def can_win_game(pots):
        score = PotsOfGold._can_win_game_helper(pots)
        print("Max score: {}".format(score))
        return score > 0

    @staticmethod
    def _can_win_game_helper(pots):
        if not pots:
            return 0
        pick_left = pots[0] - PotsOfGold._can_win_game_helper(pots[1:])
        pick_right = pots[-1] - PotsOfGold._can_win_game_helper(pots[:len(pots)-1])
        return max(pick_left, pick_right)


class TestPotsOfGold(object):
    can_win = [20, 90, 90, 10]
    can_not_win = [10, 90, 10, 90, 10]

    def test_pots_of_gold(self):
        assert PotsOfGold.can_win_game(self.can_win)
        assert not PotsOfGold.can_win_game(self.can_not_win)