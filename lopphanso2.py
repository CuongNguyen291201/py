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
    arr = list(int(i) for i in input().split())
    a = arr[0]*arr[len(arr)-1] + arr[len(arr)-2]*arr[1]
    b = arr[1]*arr[len(arr)-1]
    p = PhanSo(a, b)
    p.result()
main()