#!/usr/bin/env python3

from flask import Flask, request
from markupsafe import escape, Markup

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>')
def print_string(hello):
    print("hello")
    return Markup.escape(hello)

@app.route('/count/<int:count>')
def count(count):
    count_range = range(0, 10)
    count_string = '\n'.join(str(i) for i in count_range)
    return Markup.escape(count_string)


@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)