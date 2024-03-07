# write your code here
import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students_count = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            current_students_count = len(group.students)
            max_students_count = max(max_students_count, current_students_count)
    return max_students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)

def read_students_information():
    students = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                students.append(student)
        except EOFError:
            pass
    return students

def read_groups_information():
    specialties = set()  # Множество для хранения уникальных специальностей
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)



