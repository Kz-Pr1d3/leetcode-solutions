def is_valid(s: str) -> bool:
    opening = '({['
    closing = ')}]'
    parentheses_pairs = {')': '(', '}': '{', ']': '['}
    check = []
    for char in s:
        if char in opening:
            check.append(char)
        elif char in closing:
            if len(check) == 0:
                return False
            open_pair = parentheses_pairs[char]
            if check[-1] == open_pair:
                check.pop()
            else:
                return False

    if len(check) == 0:
        return True
    else:
        return False


s = "()"
result = is_valid(s=s)
print(result)
# assert result == True

s = "()[]{}"
result = is_valid(s=s)
print(result)
# assert result == True

s = "(]"
result = is_valid(s=s)
print(result)
# assert result == False

s = "([)]"
result = is_valid(s=s)
print(result)
# assert result == False

s = "{[]}"
result = is_valid(s=s)
print(result)
# assert result == True

s = '(])'
result = is_valid(s=s)
print(result)