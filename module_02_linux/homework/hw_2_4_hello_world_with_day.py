"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<name>")
def hello_world(name) -> str:
    week_days = ['нет дня с индексом 0', 'хорошего  понедельника', 'хорошего вторника', 'хорошей среды',
                 'хорошего четверга', 'хорошей пятницы', 'хорошей субботы', 'хорошего воскресенья']
    return f"Привет, {name},  {week_days[datetime.datetime.today().isoweekday()]}!"


if __name__ == "__main__":
    app.run(debug=True)
