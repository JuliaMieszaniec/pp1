class Student():
    university="Uek"
    id=100000

    def __init__(self, name, surname, field):
        self.name=name
        self.surname=surname
        self.id=Student.id
        Student.id+=1
        self.filed=field

    def __str__(self):
        return f"Name: {self.name} \nSurname: {self.surname} \nUni: {Student.university}\nID: {self.id}"

        

student1=Student("Olek", "Kowalski", "Human Resrorces")
student2=Student("Maks", "Jemioła", "Informatics")
print(student1)
print()
print(student2)
