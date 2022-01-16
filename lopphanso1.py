import math

class PhanSo():
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
    def result(self):
        t = self.a // math.gcd(self.a, self.b)
        m = self.b // math.gcd(self.a, self.b)

        print(f'{t}/{m}')
def main():
    a, b = map(int, input().split())
    p = PhanSo(a, b)
    p.result()
main()