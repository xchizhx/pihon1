def kot(d):
    s = d.split(",")

    for i in range(len(s)):
        if s[i] == "кот":
            return s[i]


print(kot("пёс,кит,кот,лошадь,жираф"))
