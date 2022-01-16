from datetime import datetime

class Student():
    def __init__(self, name, date, p1:float, p2:float, p3:float):
        self.name = name
        self.date = date
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def result(self):
        point = self.p1 + self.p2 + self.p3
        print(f'{self.name} {self.date} {point}')

def main():

    name = input()
    date = input()
    p1 = float(input())
    p2 = float(input())
    p3 = float(input())
    s = Student(name, date, p1, p2, p3)
    s.result()
main()