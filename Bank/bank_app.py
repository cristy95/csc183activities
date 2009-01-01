# -*- coding: utf-8 -*-
"DOCSTRING"
from flask import Flask, render_template, request
from bank.bank import Bank
from bank.account import Account
APP = Flask(__name__)
BANK = Bank()

@APP.route('/')
def hello_world():
    """Gets account and returns balance of account"""
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)

if __name__ == '__main__':

    ACCOUNT = Account('1111', 50)
    BANK.add_account(ACCOUNT)
    APP.run(debug=True)
