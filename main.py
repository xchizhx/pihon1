def kot(d, s):
    s = d.split(s)

    for i in range(len(s)):
        if s[i] == "кот":
            return s[i]


print(kot("пёс,кит,кот,лошадь,жираф", ","))
