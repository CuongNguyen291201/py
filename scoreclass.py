class Student():
    def __init__(self, name, d1, d2, d3):
        self.name = name
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        
    def result(self):
        diem = self.d1*0.1 + self.d2*0.3 + self.d3*0.6
        print(f'{self.name} {diem}')
        
def main():
    name = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    student = Student(name, d1, d2, d3)
    student.result()
main()
