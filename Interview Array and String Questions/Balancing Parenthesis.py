def balance_check(s):
    chars = []
    matches = {')':'(',']':'[','}':'{'}
    for c in s:
        if c in matches:
            if chars.pop() != matches[c]:
                return False
        else:
            chars.append(c)
    return chars == []
    pass


print(balance_check("[]"))
print(balance_check("[()]"))
