
class Rectangle():
    def __init__(self, length: int, deep: int, color: str):
        self.length = length
        self.deep = deep
        self.color = color
    def result(self):
        s = self.length * self.deep
        p = (self.length + self.deep) * 2
        print(f'{p} {s} {self.color.title()}')
    
def main():
    a = []
    while len(a) < 3:
        for i in input().split():
            a.append(i)
    if a[0].isdigit() and a[1].isdigit(): 
        rec = Rectangle(int(a[0]), int(a[1]), a[2])
        rec.result()
    else: print('INVALID')
main()