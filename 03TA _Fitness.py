from datetime import datetime

def main():
    gender = input("Please type your gender (Male/Female): ")
    birthdate =(input("Please type yout birthdate in this format YYYY-MM-DD: "))
    weight = float(input("Please type your weight in pounds: "))
    height = float(input("Please type your height in inches: "))
    print()
    age = compute_age(birthdate)
    kg = lb_to_kg(weight)
    cm = in_to_cm(height)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, age)
    print(f"Gender: {gender.capitalize()}")
    print(f"Age: {age} years")
    print(f"Weight in kg: {kg:.2f}")
    print(f"Height in cm: {cm:.2f}")
    print(f"Body Mass Index: {bmi:.2f}")
    print(f"Basal Metabolic Rate: {bmr:.2f}")

def compute_age(birthdate):

    birthday = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    age = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        age -= 1

    return age

def lb_to_kg(weight):
    kg = float(weight/2.205)
    return kg

def in_to_cm(height):
    cm = float(height * 2.54)
    return cm

def body_mass_index(kg, cm):
    bmi = (float(10000 * kg)/cm**2)
    return bmi

def basal_metabolic_rate(gender,kg,cm, age):
    if gender.lower() == "male":
        bmr = float(88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * age))
        return bmr
    elif gender.lower() == "female":
        bmr = float(447.593 + (9.247 * kg) + (3.098 * cm) - (4.330 * age))
        return bmr

main()
