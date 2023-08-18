def kot():
    d = "пёс,кит,кот,лошадь,жираф"
    s = d.split(",")

    for i in range(len(s)):
        if s[i] == "кот":
            return s[i]


print(kot())
