def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000,
    }

    arab_nums = []
    for char in s:
        arab_nums.append(roman_values[char])


    new_num = 0
    for i in range(len(arab_nums)):
        # if i != (len(arab_nums) - 1):
        now = arab_nums[i]
        next = arab_nums[i + 1]

        if now < next:
            new_num += next - now
            i += 2

        if now >= next:
            new_num += now

    print(arab_nums)
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
