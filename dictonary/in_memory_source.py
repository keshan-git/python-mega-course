import os
import json
from difflib import get_close_matches


class InMemorySource:
    def __init__(self):
        self.file_name = 'data/data.json'
        self.data = self.__generate_data()

    def get_suggestions(self, term):
        term = self.__pre_process(term)
        return get_close_matches(term, self.data.keys(), n=5, cutoff=0.5)

    def find(self, term):
        term = self.__pre_process(term)
        if term in self.data:
            return self.data[term]

    def __generate_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                content = json.load(file)

            content = {key.lower(): value for key, value in content.items()}
        else:
            print('Unable to find the data file={}'.format(self.file_name))
        return content

    @staticmethod
    def __pre_process(term):
        return term.lower()



