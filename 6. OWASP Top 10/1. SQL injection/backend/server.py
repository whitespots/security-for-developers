import os
import sqlite3
from flask import Blueprint, jsonify, request


sql_injection_1 = Blueprint('sql_injection_1', __name__)


@sql_injection_1.route('/labs/sql_injection_1/auth', methods=['GET', 'POST'])
def auth():
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
