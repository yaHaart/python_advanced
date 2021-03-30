import datetime
from random import choice, randint
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def test_function():
    return 'Hello World!'


@app.route('/cars')
def cars():
    cars = 'Chevrolet, Renault, Ford, Lada'
    return cars


@app.route('/cats')
def cats():
    cat = choice(['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мэйн-Кун', 'Манчкин'])
    return cat


@app.route('/get_time/now')
def time_now():
    return str(datetime.datetime.now())


@app.route('/get_time/future')
def time_future():
    time_now = datetime.datetime.now()
    time_future = time_now + datetime.timedelta(hours=1)
    return str(time_future)


@app.route('/get_random_word')
def random_word():
    # TODO При написании веб сервисов нужно стараться уменьшить время ожидания ответа клиентом.
    #  Сейчас при каждом вызове файл полностью прочитывается, разбирается
    #  на строки из выбранной строки выбирается слова.
    #  Можно при запуске всего приложения или первом запросе к эндпоинту
    #  разделять файл и выбирать из него все подходящие слова, сохраняя их в один
    #  список. При последующих запросах останется из готового списка
    #  случайно выбирать слово.
    #  На данном этапе список удобнее будет хранить в глобальной переменной.
    with open('voyna-i-mir.txt', 'r', encoding='UTF-8') as file:
        text = file.readlines()
    random_line_number = randint(0, len(text))
    random_line = text[random_line_number - 1]
    random_word = choice(random_line.split())
    return random_word


@app.route('/counter')
def counter():
    global count
    count += 1
    return 'страница запускалась ' + str(count) + ' раз'


count = 0
if __name__ == "__main__":
    app.run()
