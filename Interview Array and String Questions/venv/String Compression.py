def compress(s):
    r = ''
    l = len(s)

    if l == 0:
        return ''
    else:

    if l == 1:
        return s + '1'
    count = 1
    i = 1

    while i < l:
        if s[i] == s[i + 1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
        i += 1
    r = r + s[i-1] + str(count)
    return r
    pass


compress("AAAAAABBBBBBB")