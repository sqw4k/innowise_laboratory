def find_student(students_list: list[dict], student_name: str) -> dict | None:
    # Check for empty input data
    if not student_name or not students_list:
        return None
    result = next(
        (student for student in students_list
         if student["student_name"] == student_name.lower()),
        None
    )
    return result


def new_student(students_list: list[dict]) -> None:
    student_name = input("Enter student name: ").strip()
    if not student_name:
        print("Student name cannot be empty!")
        return

    if find_student(students_list, student_name):
        print("Student already exists!")
    else:
        student_data = {
            "student_name": student_name.lower(),
            "student_grade": [],
        }
        students_list.append(student_data)
        print(f"Student {student_name} added successfully!")


def add_grades(students_list: list[dict]) -> None:
    # Check if there are any students in the system
    if not students_list:
        print("No students available! Add students first.")
        return

    student_name = input("Enter student name: ").strip()
    if not student_name:
        print("Student name cannot be empty!")
        return

    student_data = find_student(students_list, student_name)
    if student_data:
        while True:
            grade = input("Enter a grade (or 'done' to finish): ").strip()
            if not grade:
                continue
            if grade.lower() == 'done':
                break
            try:
                current_grade = int(grade)
                if 0 <= current_grade <= 100:
                    student_data["student_grade"].append(current_grade)
                    print(f"Grade {current_grade} added successfully!")
                else:
                    print("Grade must be between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")
    else:
        print("Student doesn't exist!")


def calculate_averages(students_list: list[dict]) -> None:
    # Calculate averages for all students
    for student in students_list:
        grades = student["student_grade"]
        if grades:
            student["student_avg"] = sum(grades) / len(grades)
        else:
            student["student_avg"] = "N/A"


def max_avg_grade(students_list: list[dict]) -> float | None:
    if not students_list:
        return None
    students_with_grades = [
        student for student in students_list
        if student.get("student_avg", "N/A") != "N/A"
           and isinstance(student.get("student_avg", "N/A"), (int, float))
    ]
    if not students_with_grades:
        return None
    max_student = max(students_with_grades, key=lambda x: x["student_avg"])
    return max_student["student_avg"]


def max_avg_student(students_list: list[dict]) -> str | None:
    if not students_list:
        return None
    students_with_grades = [
        student for student in students_list
        if student.get("student_avg", "N/A") != "N/A"
           and isinstance(student.get("student_avg", "N/A"), (int, float))
    ]
    if not students_with_grades:
        return None
    max_student = max(students_with_grades, key=lambda x: x["student_avg"])
    return max_student["student_name"]


def min_avg_grade(students_list: list[dict]) -> float | None:
    if not students_list:
        return None
    students_with_grades = [
        student for student in students_list
        if student.get("student_avg", "N/A") != "N/A"
           and isinstance(student.get("student_avg", "N/A"), (int, float))
    ]
    if not students_with_grades:
        return None
    min_student = min(students_with_grades, key=lambda x: x["student_avg"])
    return min_student["student_avg"]


def overall_grade(students_list: list[dict]) -> float | None:
    if not students_list:
        return None

    all_grades = []
    for student in students_list:
        all_grades.extend(student.get("student_grade", []))

    if not all_grades:
        return None

    return sum(all_grades) / len(all_grades)


def avg_grades(students_list: list[dict]) -> None:
    if not students_list:
        print("No students available!")
        return

    # Calculate averages before generating report
    calculate_averages(students_list)

    print("--- Student Report ---")

    for student_data in students_list:
        avg = student_data.get("student_avg", "N/A")
        name = student_data["student_name"].capitalize()

        if avg == "N/A":
            print(f"{name}'s average grade is N/A")
        else:
            print(f"{name}'s average grade is {avg:.1f}")

    print("------------------------")

    max_avg = max_avg_grade(students_list)
    min_avg = min_avg_grade(students_list)
    overall_avg = overall_grade(students_list)

    print(f"Max Average: {max_avg if max_avg is not None else 'N/A'}")
    print(f"Min Average: {min_avg if min_avg is not None else 'N/A'}")
    print(f"Overall Average: {overall_avg if overall_avg is not None else 'N/A'}")


def main() -> None:
    students = []

    while True:
        print("\n-------- Student Grade Analyzer -----------")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit the program")

        choice_input = input("Enter your choice: ").strip()
        if not choice_input:
            print("Please enter a choice!")
            continue

        try:
            choice = int(choice_input)
        except ValueError:
            print("Please enter a number from 1 to 5!")
            continue

        if not 1 <= choice <= 5:
            print("Invalid choice!")
            continue

        match choice:
            case 1:
                new_student(students)
            case 2:
                add_grades(students)
            case 3:
                avg_grades(students)
            case 4:
                if not students:
                    print("No students available!")
                else:
                    # Calculate averages before finding top student
                    calculate_averages(students)
                    top_student_name = max_avg_student(students)
                    top_grade_value = max_avg_grade(students)
                    if top_student_name and top_grade_value is not None:
                        name = top_student_name.capitalize()
                        print(f"The student with the highest average is {name} "
                              f"with a grade of {top_grade_value:.1f}")
                    else:
                        print("No students with grades available!")
            case 5:
                print("Exiting program")
                break


if __name__ == "__main__":
    main()