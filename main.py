def kot():
    d = "пёс,кит,кот,лошадь,жираф"
    s = d.split(",")

    for i in range(len(s)):
        if d[i] == "кот":
            return d[i]


print(kot())
