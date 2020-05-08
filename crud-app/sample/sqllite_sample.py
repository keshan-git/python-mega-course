import sqlite3 as sql


def create_connection():
    connection = sql.connect('lite.db')
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    connection.commit()
    connection.close()


def insert_data(item, quantity, price):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO store VALUES(?, ?, ?)', (item, quantity, price))
    connection.commit()
    connection.close()


def update_data(item, quantity, price):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))
    connection.commit()
    connection.close()


def delete_data(item):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM store WHERE item=?', (item,))
    connection.commit()
    connection.close()


def view_data():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM store')
    result = cursor.fetchall()
    connection.close()
    return result


def main():
    # insert_data('Coffee Cup', 10, 5)
    print(view_data())
    delete_data('wine Glass')
    update_data('Coffee Cup', 20, 6)
    print(view_data())


if __name__ == '__main__':
    main()