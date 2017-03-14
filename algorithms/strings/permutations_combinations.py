from collections import Counter

c = Counter("aabc")

def _permutate(char_counts, input_str, sub_str):
    if len(sub_str) == len(input_str):
        print sub_str
    else:
        for char in sorted(char_counts):
            if char_counts[char] != 0:
                char_counts[char] -= 1
                _permutate(char_counts, input_str, sub_str + char)
                char_counts[char] += 1

def permutate(input_str):
    _permutate(Counter(input_str), input_str, '')

def _permutate_other(input_str, sub_str):
    if not input_str:
        print sub_str
    else:
        for x in range(len(input_str)):
            _permutate_other(input_str[:x] + input_str[x+1:], sub_str + input_str[x])

def permutate_other(input_str):
    _permutate_other(input_str, '')

def _character_combinations(char_counts, input_str, sub_str, level):
    if len(sub_str) == len(input_str):
        return
    else:
        for char in sorted(char_counts):
            if char_counts[char] != 0:
                print sub_str + char
                char_counts[char] -= 1
                _character_combinations(char_counts, input_str, sub_str + char, level)
                char_counts[char] += 1


def character_combinations(input_str):
    _character_combinations(Counter(input_str), input_str, '', 0)

print("Method 1:")
permutate("aabc")
print("\nMethod 2:")
permutate_other("aabc")
print("\nCharacter combinations:")
character_combinations("abc")