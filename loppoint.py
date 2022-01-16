import math

class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def result(self):
        res = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        result = '{0:.4f}'.format(res)
        print(result)

def main():
    for i in range(int(input())):
        arr = input().split()
        point = Point(float(arr[0]), float(arr[1]), float(arr[2]), float(arr[3]))
        point.result()

main()
