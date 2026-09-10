# Problem 5
role = input("Enter your role (Student / Teacher): ").lower().strip()
age = int(input("Enter your age: "))
print(f"Eligible : {role == "student" and age < 21}")