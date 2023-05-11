import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def sql_injection():
    if request.method == 'POST':
        try:
            login = request.values.get('login')
            password = request.values.get('password')

            connection = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.db'))
            cursor = connection.cursor()
            cursor.execute('select * from users where login = "' + login + '" and pass = "' + password + '";')
            user = cursor.fetchone()
            if user:
                if user[1] == 'admin':
                    return jsonify({'login': user[1], 'flag': 'c6e5460a7133df2dfaf06e8835995a67'})
                return jsonify({'login': user[1]})
            else:
                return jsonify({'error': 'Invalid credentials'})
        except BaseException:
            return jsonify({'error': 'Invalid credentials'})
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)