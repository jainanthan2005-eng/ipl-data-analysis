class Student:
    def __init__(self,name,marks):
        self.name=name                #instance variable
        self.marks=marks              #instance variable(list)

    def average(self):                #instance method
        return sum(self.marks) /    len(self.marks)
    def grade(self):
        avg=self.average()
        if avg >=90: return 'A+'
        elif avg>=80: return 'A'
        elif avg>70: return 'B'
        elif avg>=60: return'C'
        else: return 'F'

    def display(self):                #instance.method
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")
        
                         
 #Main
s=Student('Jainanthan',[85,87,
98,98,99])
s.display()
           


        
