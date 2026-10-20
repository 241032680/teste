import array

def initstat(n=1):
    if n == 1:
        return array.array('b', [0]*8)
    else:
        return (array.array('b', [0]*8) for _ in range(n))

def getstat(stat):
    return sum(stat)


rolls = initstat()
print(rolls)
foo, bar = initstat(2)
foo[0] = 12
print(foo, bar)
bar[0] = 10
print(foo, bar)
def roll(teste):
    stat = getstat(teste)
    bonus = stat%5 + getstat(rolls)
    print(bonus)


print(getstat(foo))


def bar(val_list, value=0):
    # Dynamically build a string like "a, b, c = 0, 0, 0"
    names = ", ".join(val_list)
    values = ", ".join([str(value)] * len(val_list))
    
    # Execute the assignment statement
    exec(f"{names} = {values}", globals())

foo = ('a', 'b', 'c')
bar(foo)

# Now the variables exist globally:
print(a)  # 0
print(b)  # 0
print(c)  # 0