import sys

class CannotMakeChange(Exception):
    pass

def get_min_num_coins(coins, target):
    matrix = [0] + [sys.maxint] * target
    matrix2 = [-1] * (target+1)
    for idx, coin in enumerate(coins):
        for x in range(coin, target+1):
            new_val = min(matrix[x], 1 + matrix[x - coin])
            if new_val < matrix[x]:
                matrix[x] = new_val
                matrix2[x] = idx
    if matrix[target] == sys.maxint:
        raise CannotMakeChange("Cannot reach {} with coins.".format(target))
    else:
        coins_to_make_target = []
        while target != 0:
            coins_to_make_target.append(coins[matrix2[target]])
            target -= coins[matrix2[target]]
        return coins_to_make_target

class Solution(object):
    def coinChange(self, coins, amount):
        try:
            num_coins = len(get_min_num_coins(coins, amount))
            return num_coins
        except CannotMakeChange:
            return -1

class TestCoinChange(object):
    def test_coin_change(self):
        import pytest
        assert get_min_num_coins([7, 2, 3, 6], 13) == [6, 7]
        assert get_min_num_coins([1, 2, 5], 11) == [5, 5, 1]
        with pytest.raises(CannotMakeChange):
            assert get_min_num_coins([2], 3) == []
        with pytest.raises(CannotMakeChange):
            assert get_min_num_coins([2], 1) == []
        # assert get_min_num_coins([186,419,83,408], 6249) == 20