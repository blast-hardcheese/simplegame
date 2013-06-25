Space = 0
Wall = 1
Start = 2
End = 3
Player = 4

Characters = {
    Space: " ",
    Wall: "#",
    Start: "S",
    End: "E",
    Player: "@",
}

for key in Characters.keys():
    value = Characters[key]
    Characters[value] = key
