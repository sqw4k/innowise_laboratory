def find_student(list_of_students: list[dict], current_student_name: str) -> dict | None:
    result: dict | None = next((existing_student for existing_student in list_of_students
                   if existing_student["student_name"] == current_student_name.lower()), None)
    return result

def find_student_index(list_of_students: list[dict], current_student_data: dict) -> int:
    i: int
    for i, existing_student_data in enumerate(list_of_students):
        if existing_student_data == current_student_data:
            return i
    return -1

def new_student(list_of_students: list[dict]) -> list[dict] | None:
    student_name: str = input("Enter student name: ")
    if find_student(list_of_students, student_name):
        student_data: dict = {
            "student_name": student_name.lower(),
            "student_grade": list,
        }
        return list_of_students.append(student_data)
    else:
        print("Student already exists!")
        return None

def add_grades(list_of_grades: list[dict]) -> list[dict] | None:
    student_name: str = input("Enter student name: ")
    current_student_data: dict = find_student(list_of_grades, student_name)
    if current_student_data:
        while True:
            grade: str = input("Enter a grade (or 'done' to finish): ")
            if grade == "done":
                return list_of_grades
            try:
                current_grade: int = int(grade)
                list_of_grades[find_student_index(list_of_grades, current_student_data)]["student_grade"].append(current_grade)
            except ValueError:
                print("Type a valid grade with integers!")
                return list_of_grades
    else:
        print("Student doesn't exist!")
        return None

def max_avg_grade(list_of_grades: list[dict]) -> float | None:
    max_student = max(list_of_grades, key=lambda x: x["student_avg"])
    try:
        max_avg: float = max_student["student_avg"]
        return max_avg
    except ValueError:
        print("{Your students have no grades!")
        return None

def max_avg_student(list_of_grades: list[dict]) -> str | None:
    max_student = max(list_of_grades, key=lambda x: x["student_avg"])
    try:
        max_avg: float = max_student["student_avg"]
        return max_student["student_name"]
    except ValueError:
        print("{Your students have no grades!")
        return None

def min_avg_grade(list_of_grades: list[dict]) -> float | None:
    min_student = min(list_of_grades, key=lambda x: x["student_avg"])
    try:
        min_avg: float = min_student["student_avg"]
        return min_avg
    except ValueError:
        print("{Your students have no grades!")
        return None

def overall_grade(list_of_grades: list[dict]) -> float | None:
    summ: float = 0
    for avg_grade in list_of_grades:
        summ += avg_grade["student_avg"]
    try:
        overall_grade: float = summ / len(list_of_grades) + 1
        return overall_grade
    except ZeroDivisionError:
        return None

def avg_grades(list_of_avgs: list[dict]) -> list[dict]:
    for existing_student_data in list_of_avgs:
        index: int = find_student_index(list_of_avgs, existing_student_data)
        list_of_avgs[index]["student_avg"]: str = "N/A"
        summ: int = 0
        quantity: int = 0
        for grade in existing_student_data["student_grade"]:
            summ = summ + list_of_avgs[index]["student_grade"][grade]
            quantity = quantity + 1
        try:
            list_of_avgs[index]["student_avg"]: float = (summ / quantity)
            print(f"{existing_student_data['student_name'].capitalize()}'s average grade is {existing_student_data['student_avg']}")
        except ZeroDivisionError:
            print(f"{existing_student_data['student_name'].capitalize()}'s average grade is N/A")
    print(f"------------------------"
          f"Max Average: {max_avg_grade(list_of_avgs)}"
          f"Min Average: {min_avg_grade(list_of_avgs)}"
          f"Overall Average: {overall_grade(list_of_avgs)}")




def main():
    students: list[dict] = []
    print("--------Student Grade Analyzer-----------"
          "1. Add a new student"
          "2. Add grades for a student"
          "3. Generate a full report"
          "4. Find the top student"
          "5. Exit the program")
    while True:
        label = input("Enter your choice: ")
        try:
            label = int(label)
        except ValueError:
            print("Enter an int from 1 to 5!")
            continue
        if not 1 <= label <= 5:
            print("Invalid choice!")
            continue
        match label:
            case 1:
                print("Enter the student name: ")
                new_student(students)
            case 2:
                add_grades(students)
            case 3:
                avg_grades(students)
            case 4:
                if max_avg_student(students):
                    print(f"The student with the highest average is {max_avg_student(students).capitalize()} with a grade of {max_avg_grade(students)}")
                else:
                    print("{Your students have no grades!")
            case 5:
                quit("Leaving program")


if __name__ == "__main__":
    main()