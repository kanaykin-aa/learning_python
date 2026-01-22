def bmi(weight, height):
    fbmi=weight/height**2
    if fbmi<=18.5:
        return "Underweight"
    elif fbmi<=25.0:
        return "Normal"
    elif fbmi<=30:
        return "Overweight"
    else:
        return "Obese"