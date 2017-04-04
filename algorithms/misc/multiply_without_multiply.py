
def _multiply_helper(smaller, larger):
    if not smaller:
        return 0
    elif smaller == 1:
        return larger

    half_prod = _multiply_helper(smaller/2, larger)

    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + larger


def multiply(num1, num2):
    if num1 < num2:
        return _multiply_helper(num1, num2)
    else:
        return _multiply_helper(num2, num1)


class TestMultiplyWithoutMultiply(object):
    def test_multiply_without_multiply(self):
        assert multiply(5, 6) == 30
        assert multiply(1, 100) == 100
        assert multiply(100, 1) == 100
        assert multiply(100, 0) == 0
