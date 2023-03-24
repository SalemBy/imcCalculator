def turnToFloat(real):
    return float(real.replace(',','.'))

def checkValue():

    while True:
        try:

            height = turnToFloat(str(input('Please enter your height: ')))
            weight = turnToFloat(str(input('Please, enter your weight: ')))
            bmi = (weight / (height**2))
            if bmi < 18.5 :
                healthy = 'Underweight'
            if bmi >= 18.5 <= 24.9:
                healthy = 'Normal'
            if bmi >= 25 <= 29.9:
                healthy = 'Overweight'
            if bmi >= 30 <= 34.9:
                healthy = 'Obese'
            if bmi >= 35:
                healthy = 'Extremely Obese'

            first_line = f"Your BMI is around {bmi:.2f}. "
            second_line = f"Your BMI is {healthy}"

            print(first_line)
            print(second_line)
        except ValueError:
            print("Please, enter only numbers.")
            continue
        break



checkValue()
