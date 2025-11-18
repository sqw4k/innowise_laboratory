from datetime import datetime


def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


def main():
    print("Welcome to Mini-Profile Generator!")
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)

    now = datetime.now()
    if now.year - birth_year >= 135:
        raise SystemExit("You entered the wrong year, are you still alive? Try again.")

    current_age = now.year - birth_year

    hobbies = []
    hobby = ""
    while True:
        hobby = input("Enter a favourite hobby or type 'stop' to finish: ")
        if hobby == "stop":
            break
        hobbies.append(hobby)

    life_stage = generate_profile(current_age)
    user_profile = {
        "user_name": user_name,
        "age": current_age,
        "life_stage": life_stage,
        "favourite_hobbies": hobbies,
    }
    print(" \n--- \nProfile Summary:")
    print(f"Name: {user_profile['user_name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")
    if not hobbies:
        print("You didn't mention any hobbies. \n ---")
    else:
        print(f"Favourite Hobbies({len(hobbies)}): ")
        for hobby in user_profile["favourite_hobbies"]:
            print(f"- {hobby}")
        print("---")


if __name__ == "__main__":
    main()
