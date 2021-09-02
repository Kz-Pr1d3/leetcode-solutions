def roman_to_int_old(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000,
    }
    arab_nums = []
    for char in s:
        arab_nums.append(roman_values[char])
    arab_length = len(arab_nums)
    new_num = 0
    previous_num = 0
    for i in range(arab_length-1, -1, -1):
        now = arab_nums[i]
        if previous_num > now:
            new_num -= now
        if previous_num <= now:
            new_num += now
        previous_num = now
    return new_num


def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000,
    }
    new_num = 0
    previous_num = 0
    for i in reversed(s):
        now = roman_values[i]
        if previous_num > now:
            new_num -= now
        if previous_num <= now:
            new_num += now
        previous_num = now
    return new_num


s = "III"
result = roman_to_int(s=s)
print(result)

s = "IV"
result = roman_to_int(s=s)
print(result)

s = "IX"
result = roman_to_int(s=s)
print(result)

s = "LVIII"
result = roman_to_int(s=s)
print(result)

s = "MCMXCIV"
result = roman_to_int(s=s)
print(result)
