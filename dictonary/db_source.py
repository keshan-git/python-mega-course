import os
import json
import mysql.connector
from mysql.connector import errorcode
from difflib import get_close_matches


class DBSource:
    def __init__(self):
        self.ready = False
        self.connection = self.__create_db_connection()
        self.file_name = 'data/data.json'
        self.word_list = []
        if self.ready:
            self.__populate_data()

    def find(self, term):
        term = self.__pre_process(term)

        cursor = self.connection.cursor()
        query = 'SELECT word, definition FROM data_definitions WHERE word = %s'
        cursor.execute(query, (term, ))
        result = []
        for (word, definition) in cursor:
            result.append(definition)

        cursor.close()
        if result:
            return result

    def get_suggestions(self, term):
        term = self.__pre_process(term)
        if not self.word_list:
            self.__populate_word_list()
        return get_close_matches(term, self.word_list, n=5, cutoff=0.5)

    def __create_db_connection(self):
        try:
            connection = mysql.connector.connect(user='root',
                                                 password='root',
                                                 host='127.0.0.1',
                                                 port='2012',
                                                 database='definition')
            print("Database connection created [{}]".format(connection.server_host))
            self.ready = True
            return connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid credentials for the database")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def __generate_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                content = json.load(file)

            content = {key.lower(): value for key, value in content.items()}
        else:
            print('Unable to find the data file={}'.format(self.file_name))
        return content

    def __populate_data(self):
        # check if data base is already populated
        cursor = self.connection.cursor()
        query = 'SELECT COUNT(*)FROM data_definitions'
        cursor.execute(query)
        is_db_empty = False

        for count in cursor:
            print('Found {} data records in the database'.format(count))
            if count[0] == 0:
                is_db_empty = True
        cursor.close()

        if is_db_empty:
            print('Population data-base with the data')
            data = self.__generate_data()

            cursor = self.connection.cursor()
            add_entry = 'INSERT INTO data_definitions (word, definition) VALUES (%s, %s)'
            for word, definitions in data.items():
                for definition in definitions:
                    cursor.execute(add_entry, (word.lower(), definition))
                row_id = cursor.lastrowid
                if row_id % 100 == 0:
                    print('\rInserting definition data to the Database [{}]'.format(row_id), end="", flush=True)
            self.connection.commit()
            cursor.close()

            print('\nPopulation data-base with the data - Done')

    def __populate_word_list(self):
        cursor = self.connection.cursor()
        query = 'SELECT DISTINCT(word) FROM data_definitions'
        cursor.execute(query)
        for word in cursor:
            self.word_list.append(word[0])
        cursor.close()

    @staticmethod
    def __pre_process(term):
        return term.lower()



