def kot(d, sep):
    s = d.split(sep)

    for i in range(len(s)):
        if s[i] == "кот":
            return s[i]


print(kot("пёс,кит,кот,лошадь,жираф", ","))
