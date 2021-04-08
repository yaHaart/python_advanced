"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<num1>/<num2>/<num3>/")
# TODO Лучше получить список чисел в одну переменную:
#  "/max_number/<path:numbers>/")
#  Тогда в переменной numbers будет строка, содержащая числа разделенные слэшами.
def max_number(num1, num2, num3):

    return f'Максимальное переданное число <i>{max(num1, num2, num3)}</i>'


if __name__ == "__main__":
    app.run(debug=True)
