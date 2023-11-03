def make_student(id, name):
    return [id, name, 0, 0.0]

def add_student(student_list, id, name):
    for index in range(len(student_list)):
        if student_list[index][0] == id:
            student_list.pop(index)
            break
    student_list.append(make_student(id, name))


def main():
    students = []
    add_student(students, 2345, "Yoel") 
    add_student(students, 9999, "Seth")
    add_student(students, 2222, "Carlos")
    add_student(students, 1111, "Pramesh")
    
    for student in students:
        print(student)

if __name__ == "__main__":
    main()