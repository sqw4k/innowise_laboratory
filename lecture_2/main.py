from datetime import datetime

def generate_profile(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:
        return "Adult"

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
now = datetime.now()
if now.year - birth_year >= 135:
    raise SystemExit("You entered the wrong year, are you still alive? Try again.")
now = datetime.now()
current_age = now.year - birth_year
hobbies = []
hobbie = ""
hobbies_amount = 0
while hobbie != "stop" :
    hobbie = input("Enter a favourite hobby or type 'stop' to finish: ")
    if hobbie == "stop":
        break
    hobbies.append(hobbie)
    hobbies_amount += 1
life_stage = generate_profile(current_age)
user_profile = {
    "user_name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "Favourite hobbies": hobbies,
}
print(" \n--- \nProfile Summary:")
print(f"Name: {user_profile['user_name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")
if hobbies_amount == 0:
    print("You didn't mention any hobbies. \n ---")
else:
    print(f"Favourite Hobbies({hobbies_amount}): ")
    for hobby in user_profile["Favourite hobbies"]:
        print(f"{hobby}")
    print("---")
