def anagram(s,m):
    s = s.replace(' ' , '').lower()
    m = m.replace(' ', '').lower()

    if len(s) != len(m):
        return False

    counter = {}
    for i in s:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for i in m:
        if i in counter:
            counter[i] -= 1
        else:
            return False
    return True
    pass

print(anagram('dog', 'god'))