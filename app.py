from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)


# Функция для проверки номера телефона
def is_valid_phone(phone):
    if not phone:
        return False
    # Проверяем на номера Беларуси (+375) и России (+7) с цифрами
    pattern = r'^(\+375\d{9}|\+7\d{10})$'
    return bool(re.fullmatch(pattern, phone))


@app.route('/')
def index():
    return render_template('nimber.html')


@app.route('/submit_phone', methods=['POST'])
def submit_phone():
    phone = request.form.get('phone', '').strip()

    if not phone:
        return redirect(url_for('error'))

    if is_valid_phone(phone):
        try:
            with open('phones.txt', 'a', encoding='utf-8') as f:
                f.write(f"{phone}\n")
            return redirect(url_for('success'))
        except IOError:
            return "Ошибка записи в файл", 500
    else:
        return redirect(url_for('error'))


@app.route('/success')
def success():
    return "Спасибо! Ваш номер сохранён."


@app.route('/error')
def error():
    return "Ошибка: введите корректный номер (+375XXXXXXXXX или +7XXXXXXXXXX)", 400


if __name__ == '__main__':
    app.run(debug=True)