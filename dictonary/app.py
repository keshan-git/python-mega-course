from in_memory_source import InMemorySource
from db_source import DBSource


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
    source = InMemorySource()
    # source = DBSource()

    print('Welcome to the Interactive Dictionary')
    print('use /end to terminate the program')
    while True:
        input_word = input('Please enter word: ')
        if input_word == '/end':
            break

        result = source.find(input_word)
        if result:
            output(input_word, result)
            continue

        suggestions = source.get_suggestions(input_word)
        if suggestions:
            print('The word \'{}\' dose not exist. But I have few suggestions'.format(input_word))
            for idx, suggestion in enumerate(suggestions, start=1):
                print('\t ({}) - {}'.format(idx, suggestion))

            option = int(input('Please select option (0 to enter a new word): '))
            if option != 0:
                suggested_word = suggestions[option - 1]
                result = source.find(suggested_word)
                output(suggested_word, result)
            continue

        print('The word ({}) does not exist. Please double check.'.format(input_word))


if __name__ == '__main__':
    main()