

class SplitNoSpacedString(object):

    @staticmethod
    def _split_helper(word_set, input_str, memo):
        if input_str in memo:
            return memo[input_str]
        if input_str == '':
            return []
        new_word = ''
        for idx, char in enumerate(input_str):
            new_word += char
            if new_word in word_set:
                other_words = SplitNoSpacedString._split_helper(word_set, input_str[idx+1:], memo)
                if other_words is not None:
                    result = [new_word] + other_words
                    memo[input_str] = result
                    return result
        memo[input_str] = None
        return None

    @staticmethod
    def split(word_set, input_str):
        memo = {}
        return SplitNoSpacedString._split_helper(word_set, input_str, memo)

    @staticmethod
    def split_dp(word_set, input_str):
        dp = [None] * len(input_str)
        for i in xrange(len(input_str)-1, -1, -1):
            if input_str[i:] in word_set:
                dp[i] = [input_str[i:]]
                continue
            for j in xrange(i+1, len(input_str)):
                if dp[j] and input_str[i:j] in word_set:
                    dp[i] = [input_str[i:j]] + dp[j]
                    break
        return dp[0]


class TestSplitNoSpacedString(object):
    def get_words(self):
        word_set = set()
        with open('dictionary.txt', 'r') as d:
            for word in d:
                word_set.add(word.lower().strip())
        return word_set

    def test_split(self):
        words = self.get_words()
        assert SplitNoSpacedString.split(words, "onpinsandneedles") == ["on", "pin", "sand", "need", "les"]
        assert SplitNoSpacedString.split_dp(words, "onpinsandneedles") == ["on", "pin", "sand", "needles"]
        assert SplitNoSpacedString.split(words, "onpinsandneedlesq") == None