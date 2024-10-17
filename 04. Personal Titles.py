def personal_titles(gender, age):

    if gender == "m":
        if age >= 16:
            return "Mr."
        else:
            return "Master"

    elif gender == "f":
        if age >= 16:
            return "Ms."
        else:
            return "Miss"


person_age = float(input())
person_gender = input()
print(personal_titles(person_gender, person_age))
