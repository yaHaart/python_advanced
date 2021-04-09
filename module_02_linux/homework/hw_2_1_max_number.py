"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    list_of_str = numbers.split('/')
    list_of_numbers = list()
    for elem in list_of_str:
        list_of_numbers.append(int(elem))
    print(list_of_numbers)
    return f'Максимальное переданное число <i>{max(list_of_numbers)}</i>'


if __name__ == "__main__":
    app.run(debug=True)

# Зачёт!
