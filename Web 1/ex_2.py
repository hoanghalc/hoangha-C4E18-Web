from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height_cm>')
def bmi(weight,height_cm):
    height = float(height_cm/100)
    bmi = float(weight/(height*height))

    if bmi < 16:
        condition = "Severely underweight"
    elif bmi < 18.5:
        condition = "Underweight"
    elif bmi < 25:
        condition = "Normal"
    elif bmi <= 30:
        condition = "Overweight"
    else:
        condition = "Obese"
    return "Hi your bmi is {0}, you're {1}".format(str(bmi),condition)


if __name__ == '__main__':
  app.run(debug=True)
 