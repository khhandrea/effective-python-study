class Student:
    def __init__(self, name: str, birthday: str):
        self.name = name
        self.birthday = birthday

    def __repr__(self):
        return f"\nName: {self.name}, birthday: {self.birthday}"

students = (
    Student("Kim", "20040602"),
    Student("Lee", "19980723"),
    Student("Park", "20020511"),
    Student("Choi", "20000204"),
    Student("Jong", "20011127")
)

students_by_name = sorted(students, key=lambda x: x.name)
students_by_bd_name = sorted(students, key=lambda x: (x.birthday, x.name))

print(f"students sorted by name: {students_by_name}")
print(f"students sorted by birthday and name: {students_by_bd_name}")