import sqlite3 as sql
import pandas as pd

class BookService:
    def __init__(self):
        self.create_table()

    def create_connection(self):
        connection = sql.connect('book-store.db')
        return connection

    def create_table(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, '
                       'year TEXT, isbn TEXT)')
        connection.commit()
        connection.close()

    def insert_data(self, title, author, year, isbn):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO bookstore VALUES(NULL, ?, ?, ?, ?)', (title, author, year, isbn))
        connection.commit()
        connection.close()

    def view_data(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM bookstore')
        result = cursor.fetchall()
        connection.close()
        return result

    def search_data(self, title='', author='', year='', isbn=''):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
        result = cursor.fetchall()
        connection.close()
        return result

    def delete_data(self, record_id):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM bookstore WHERE id=?', (record_id,))
        connection.commit()
        connection.close()

    def update_data(self, record_id, title, author, year, isbn):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, record_id))
        connection.commit()
        connection.close()

    def populate_data(self):
        records = pd.read_csv('data/books.csv', error_bad_lines=False)
        for idx, record in records.iterrows():
            self.insert_data(record['title'], record['authors'], record['publication_date'], record['isbn'], )

            if idx % 100 == 0:
                print('{} records added to database'.format(idx))


