map = [' X '] + ["0"]*99

def avançar_nave(vel):
    x = map.index(' X ')
    map[x] = 0
    map[x+vel] = ' X '


print(f'\n{map}')
avançar_nave(7)
print(f'\n{map}')

avançar_nave(6)
print(f'\n{map}')
avançar_nave(7)
print(f'\n{map}')
avançar_nave(9)
print(f'\n{map}')
avançar_nave(8)
print(f'\n{map}')
