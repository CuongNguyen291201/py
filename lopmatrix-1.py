class Matrix(object):
    def __init__(self, a, b, c, n, m):
        self.a = a
        self.b = b
        self.c = c
        self.n = n
        self.m = m

    def result(self):
        r = self.c
        a = self.a
        b = self.b
        print(a, b)
        for i in range(self.n):
            for j in range(self.n):
                for l in range(self.m):
                    r[i][j] += a[i][l] * b[l][j]
        return r

def main():
    for i in range(int(input())):
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            a.append(list(int(i) for i in input().split()))
        b = [list(i) for i in zip(*a)]
        c = [list(i) for i in zip(*a)]
        matrix = Matrix(a, b, c, n, m)
        print(matrix.result())

main()
