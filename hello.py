print("Hello world!")

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3]
c = [i for i in a+b if i not in a or i not in b]
print(c)