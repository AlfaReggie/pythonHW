class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        lst2 = []
        for i in range(len(self.lst)):
            a = ' '.join(map(str, self.lst[i]))
            lst2.append(a)
            matrix = '\n'.join(lst2)
        return matrix

lst = [[1, 2, 3], [4, 5, 6]]
obj1 = Matrix(lst)
print(obj1)