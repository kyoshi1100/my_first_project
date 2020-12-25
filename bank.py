from random import randint
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE card ( id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0 )')


def luhn_for_tranfer(card_number_):
    digits = [int(x) for x in card_number_]
    for i in range(0, 15):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
    return 10 - sum(digits[:-1]) % 10 if sum(digits[:-1]) % 10 != 0 else 0


def luhn(card_number_):
    digits = [int(x) for x in card_number_]
    for i in range(0, 15):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
    return 10 - sum(digits) % 10 if sum(digits) % 10 != 0 else 0


def create_card():
    card_number_final = '400000' + str(randint(100000000, 999999999))
    card_number_final += str(luhn(card_number_final))
    password = str(randint(1000, 9999))
    print(
        '\nYour card has been created\nYour card number:\n{}\nYour card PIN:\n{}\n'.format(card_number_final, password))
    return {'card number': card_number_final, 'password': password}


cond = True
while cond:
    cond2 = True
    print('1. Create an account\n2. Log into account\n0. Exit')
    n = int(input())
    if n == 1:
        card = create_card()
        cur.execute('INSERT INTO card (id, number, pin) VALUES (?, ?, ?)', (1, card['card number'], card['password']))
        conn.commit()
        continue
    elif n == 2:
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        pin = input()
        if card_number not in [x[0] for x in cur.execute('SELECT number FROM card').fetchall()] or pin not in [x[0] for
                                                                                                               x in
                                                                                                               cur.execute(
                                                                                                                   'SELECT pin FROM card').fetchall()]:
            print('Wrong card number or PIN!\n')
        else:
            print('You have successfully logged in!\n')
            while cond2:
                print('\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')
                k = int(input())
                if k == 1:
                    print('Balance: ',
                          cur.execute('SELECT balance FROM card WHERE number = ?', (card_number,)).fetchone()[0])
                if k == 2:
                    print('Enter income:\n')
                    income = int(input())
                    cur.execute('UPDATE card SET balance = balance + ? WHERE number = ? ', (income, card_number))
                    conn.commit()
                    print('Income was added!')
                if k == 3:
                    print('Transfer\nEnter card number:')
                    transfer_card_number = input()
                    if luhn_for_tranfer(transfer_card_number) != [int(x) for x in transfer_card_number][15]:
                        print('Probably you made a mistake in the card number. Please try again!')
                        continue
                    if cur.execute('SELECT number FROM card WHERE number = ?',
                                   (transfer_card_number,)).fetchone() == None:
                        print('Such a card does not exist.')
                        continue
                    print('Enter how much money you want to transfer:')
                    transfer_money = int(input())
                    if transfer_money > \
                            cur.execute('SELECT balance FROM card WHERE number = ?', (card_number,)).fetchone()[0]:
                        print('Not enough money!')
                        continue
                    cur.execute('UPDATE card SET balance = balance - ? WHERE number = ?', (transfer_money, card_number))
                    cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?',
                                (transfer_money, transfer_card_number))
                    print('Success!')
                    conn.commit()
                if k == 4:
                    cur.execute('DELETE FROM card WHERE number = ?', (card_number,))
                    conn.commit()
                    cond2 = False
                if k == 5:
                    print('You have successfully logged out!\n')
                    break
                if k == 0:
                    print('Bye!')
                    cond = False
                    break
    elif n == 0:
        print('Bye!')
        break
