import os
import json
from difflib import get_close_matches


def generate_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = json.load(file)

        content = {key.lower(): value for key, value in content.items()}
    else:
        print('Unable to find the data file={}'.format(file_name))
    return content


def pre_process(term):
    return term.lower()


def get_suggestions(term, data_set):
    term = pre_process(term)
    return get_close_matches(term, data_set.keys(), n=5, cutoff=0.5)


def find(term, data_set):
    term = pre_process(term)
    if term in data_set:
        return data_set[term]


def output(word, result):
    if result:
        print('--------------------------------')
        print('Definition of {}'.format(word))
        for idx, suggestion in enumerate(result, start=1):
            print('\t ({}) - {}'.format(idx, suggestion))
        print('--------------------------------')
    else:
        print('Sorry, Unable to find the definition')


def main():
    print('Welcome to the Interactive Dictionary')
    print('use /end to terminate the program')
    data_set = generate_data('data/data.json')

    while True:
        input_word = input('Please enter word: ')
        if input_word == '/end':
            break

        result = find(input_word, data_set)
        if result:
            output(input_word, result)
            continue

        suggestions = get_suggestions(input_word, data_set)
        if suggestions:
            print('The word \'{}\' dose not exist. But I have few suggestions'.format(input_word))
            for idx, suggestion in enumerate(suggestions, start=1):
                print('\t ({}) - {}'.format(idx, suggestion))

            option = int(input('Please select option (0 to enter a new word): '))
            if option != 0:
                suggested_word = suggestions[option - 1]
                result = find(suggested_word, data_set)
                output(suggested_word, result)
            continue

        print('The word ({}) does not exist. Please double check.'.format(input_word))


if __name__ == '__main__':
    main()