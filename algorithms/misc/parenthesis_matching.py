

def match_braces(input_str):
    braces = []
    for char in input_str:
        if char in "[{(":
            braces.append(char)
        else:
            if len(braces) == 0:
                return False
            top = braces.pop()
            if char == "[" and top != "]": return False
            if char == "(" and top != ")": return False
            if char == "{" and top != "}": return False
    return len(braces) == 0

class TestBraceMatching(object):
    def test_match_braces(self):
        assert match_braces("[]")
        assert match_braces("()")
        assert match_braces("{}")
        assert not match_braces("]{}")
        assert not match_braces("{}[")
        assert match_braces("[[{[(())]}]]")
        assert not match_braces("[[[[]]]]{}{")
        assert match_braces("["*1000 + "]"*1000)