userName = input("What is Your Name? ").title().strip()
userdob = input("What is your birth year? ")


def agecal(birth_year):
    return 2026 - int(birth_year)


print(f"Hi {userName} your age is:" , agecal(userdob))