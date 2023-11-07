def make_student(id, name):
    return [id, name, 0, 0.0]

def add_student(population, id, name):
    population[id] == make_student(id, name)

def get_student(population, id):
    if id in population:
        return population[id]
    return None

def add_credits(population, id, credits):
    student = get_student(population, id)
    if student is not None:
        student[2] += credits

def get_credits(population, id):
    student = get_student(population, id)
    if student is not None:
        return student[2]

def main():
    students = {}
    add_student(students, 2345, "Yoel")
    add_student(students, 2345, "Yoel")
    add_student(students, 9999, "Seth")
    add_student(students, 2222, "Carlos")
    add_student(students, 1111, "Pramesh")

    get_student(students, 9999)
    
    # add_credits(students, 2345, 4.0)
    # print(get_credits(students, 2345))

if __name__ == "__main__":
    main()