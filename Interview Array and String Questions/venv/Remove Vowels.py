def antivowel(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")

    return newstr

print(antivowel("awejwqjkdkw"))



