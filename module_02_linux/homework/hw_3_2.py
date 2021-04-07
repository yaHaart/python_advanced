"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег
(в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    global storage
    if date in storage:
        storage[date] += number
    else:
        storage[date] = number
    return 'ok'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    global storage
    summ = 0
    for key, value in storage.items():
        if int(key[:4]) == year:
            summ += value
    return f'{summ}  рублей в {year} году'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    global storage
    summ = 0
    for key, value in storage.items():
        if int(key[:4]) == year and int(key[4:6]) == month:
            summ += value
    return f'{summ}  рублей в {month} месяце {year} года'


if __name__ == "__main__":
    app.run(debug=True)
