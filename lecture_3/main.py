"""
Student Grade Analyzer Program
Manages and analyzes student grades with menu interface.
"""


def find_student(students_list: list[dict], student_name: str) -> dict | None:
    """Find student by name in the list."""
    return next(
        (student for student in students_list
         if student["student_name"] == student_name.lower()),
        None
    )


def find_student_index(students_list: list[dict], student_data: dict) -> int:
    """Find student index in the list."""
    for index, student in enumerate(students_list):
        if student == student_data:
            return index
    return -1


def new_student(students_list: list[dict]) -> None:
    """Add a new student to the list."""
    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty!")
        return

    if find_student(students_list, student_name):
        print("Student already exists!")
        return

    student_data = {
        "student_name": student_name.lower(),
        "student_grades": [],
    }
    students_list.append(student_data)
    print(f"Student '{student_name}' added successfully!")


def add_grades(students_list: list[dict]) -> None:
    """Add grades for an existing student."""
    student_name = input("Enter student name: ").strip()
    student_data = find_student(students_list, student_name)

    if not student_data:
        print("Student doesn't exist!")
        return

    print(f"Adding grades for {student_name}:")

    while True:
        grade_input = input("Enter a grade (0-100) or 'done' to finish: ").strip()

        if grade_input.lower() == 'done':
            break

        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student_data["student_grades"].append(grade)
                print(f"Grade {grade} added.")
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")


def calculate_average(grades: list) -> float | str:
    """Calculate average of grades."""
    if not grades:
        return "N/A"
    return sum(grades) / len(grades)


def max_average_grade(students_list: list[dict]) -> float | None:
    """Find maximum average grade."""
    students_with_grades = [
        s for s in students_list
        if s.get("student_grades") and
           isinstance(calculate_average(s["student_grades"]), float)
    ]

    if not students_with_grades:
        return None

    return max(calculate_average(s["student_grades"]) for s in students_with_grades)


def max_average_student(students_list: list[dict]) -> tuple[str, float] | None:
    """Find student with highest average grade."""
    students_with_grades = [
        s for s in students_list
        if s.get("student_grades") and
           isinstance(calculate_average(s["student_grades"]), float)
    ]

    if not students_with_grades:
        return None

    top_student = max(
        students_with_grades,
        key=lambda x: calculate_average(x["student_grades"])
    )

    return (top_student["student_name"],
            calculate_average(top_student["student_grades"]))


def min_average_grade(students_list: list[dict]) -> float | None:
    """Find minimum average grade."""
    students_with_grades = [
        s for s in students_list
        if s.get("student_grades") and
           isinstance(calculate_average(s["student_grades"]), float)
    ]

    if not students_with_grades:
        return None

    return min(calculate_average(s["student_grades"]) for s in students_with_grades)


def overall_average_grade(students_list: list[dict]) -> float | None:
    """Calculate overall average grade."""
    all_grades = []
    for student in students_list:
        all_grades.extend(student.get("student_grades", []))

    if not all_grades:
        return None

    return sum(all_grades) / len(all_grades)


def generate_report(students_list: list[dict]) -> None:
    """Generate full report for all students."""
    if not students_list:
        print("No students available!")
        return

    print("\n--- Student Report ---")

    # Calculate and display individual averages
    for student in students_list:
        avg = calculate_average(student["student_grades"])
        name = student["student_name"].capitalize()

        if avg == "N/A":
            print(f"{name}'s average grade is N/A.")
        else:
            print(f"{name}'s average grade is {avg:.1f}.")

    # Display summary statistics
    print("---")

    max_avg = max_average_grade(students_list)
    min_avg = min_average_grade(students_list)
    overall_avg = overall_average_grade(students_list)

    print(f"Max Average: {max_avg if max_avg is not None else 'N/A'}")
    print(f"Min Average: {min_avg if min_avg is not None else 'N/A'}")
    print(f"Overall Average: {overall_avg if overall_avg is not None else 'N/A'}")


def main():
    """Main program function."""
    students = []

    menu = """
--- Student Grade Analyzer ---
1. Add a new student
2. Add grades for a student
3. Generate a full report
4. Find the top student
5. Exit program
----------------------------"""

    print(menu)

    while True:
        try:
            choice = input("\nEnter your choice: ").strip()

            if not choice:
                continue

            choice = int(choice)

            match choice:
                case 1:
                    new_student(students)

                case 2:
                    add_grades(students)

                case 3:
                    generate_report(students)

                case 4:
                    top_student_data = max_average_student(students)
                    if top_student_data:
                        name, grade = top_student_data
                        print(
                            f"The student with the highest average is {name.capitalize()} with a grade of {grade:.1f}.")
                    else:
                        print("No students with grades available!")

                case 5:
                    print("Exiting program.")
                    break

                case _:
                    print("Invalid choice! Please enter 1-5.")

        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break


if __name__ == "__main__":
    main()