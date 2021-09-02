import string
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    en_letters = list(string.ascii_lowercase)
    v1 = [0] * len(en_letters)
    letters_count = dict(zip(en_letters, v1))
    new_dict = {}
    for i in range(0, 200):
        new_dict[i] = letters_count

    for word in strs:
        for i in range(len(word)):
            letter = word[i]
            value = new_dict[i]
            value[letter] += 1
            new_dict[i] = value


    print(new_dict)



strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs=strs)
print(result)

strs = ["dog", "racecar", "car"]
result = longest_common_prefix(strs=strs)
print(result)
