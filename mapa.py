map = [[["X"] + ["0"]*9],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10],
    [["0"]*10]
]

def avançar_nave():
    x = map.index(7)
    map[x] = 0
    map[x+1] = 7

print(map)
avançar_nave()
print(map)

avançar_nave()
print(map)
avançar_nave()
print(map)
avançar_nave()
print(map)
avançar_nave()
print(map)