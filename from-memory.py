userName = input("What is Your Name? ").title().strip()
userdob = input("What is your birth year ")

age = 2026 - int(userdob)


print(f"Hi {userName} your age is: {age}")