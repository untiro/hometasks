class Grid:
    def __init__(self, width, height):
        self.grid = '\n'.join(list(''.join(list('0' for i in range(width))) for j in range(height)))

    def plot_point(self, x, y):
        a = self.grid.split()
        dl = len(a[0])
        b = list(a[y - 1][i] if i != (x - 1) else 'X' for i in range(dl))
        a[y - 1] = ''.join(b)
        self.grid = '\n'.join(a)

    def __repr__(self):
        print(self.grid)


g = Grid(10, 10)
g.plot_point(5, 1)
g.__repr__()
