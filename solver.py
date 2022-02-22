import loader

words = loader.load_words()

simple = words['simple']
advanced = words['advanced']

"""
Create dictionary.txt
"""
# import json
#
# f = open("five_letter_words.txt")
# words = list(f.read().split())
#
# f_simple = open("five_letter_words_simple.txt")
# simple_words = list(f_simple.read().split())
#
# for simple_word in simple_words:
#     if simple_word in words:
#         words.remove(simple_word)
#
# word_dictionary = {
#     "simple": simple_words,
#     "advanced": words
# }
#
# f = open("dictionary.txt", "w")
# f.write(json.dumps(word_dictionary, indent=4))
# f.close()

"""
Solve Wordle
"""

# ..... Correct letter, correct position: _
# ... Correct letter, incorrect position: ?
# ..................... Incorrect letter: *

allowed_symbols = ['_', '?', '*']

win = True
final_word = ['_', '_', '_', '_', '_']
incorrect_letters = []
incorrect_positions = [
    [],  # 0
    [],  # 1
    [],  # 2
    [],  # 3
    []  # 4
]


def suggestWord(w):
    return ((w[0] not in incorrect_positions[0]) and
            (w[1] not in incorrect_positions[1]) and
            (w[2] not in incorrect_positions[2]) and
            (w[3] not in incorrect_positions[3]) and
            (w[4] not in incorrect_positions[4]) and
            (w[0] not in incorrect_letters) and
            (w[1] not in incorrect_letters) and
            (w[2] not in incorrect_letters) and
            (w[3] not in incorrect_letters) and
            (w[4] not in incorrect_letters) and
            (w[0] == final_word[0] if final_word[0] != '_' else True) and
            (w[1] == final_word[1] if final_word[1] != '_' else True) and
            (w[2] == final_word[2] if final_word[2] != '_' else True) and
            (w[3] == final_word[3] if final_word[3] != '_' else True) and
            (w[4] == final_word[4] if final_word[4] != '_' else True))


while win:
    # win = False
    user_input = input('Please enter your last try as word:symbols\n')

    if user_input == 'exit':
        print('Program exited successfully.')
        break

    letters = user_input.split(':')[0].lower()
    symbols = user_input.split(':')[1]

    retry = False

    if len(letters) != 5:
        retry = True
        print('The word you entered contains ' + str(len(letters)) + ' letters instead of 5.')

    if len(symbols) != 5:
        retry = True
        print('The number of symbols you entered is ' + str(len(symbols)) + ' instead of 5.')

    if not all(c in allowed_symbols for c in symbols):
        retry = True
        print('You have entered a character that is not allowed. Please, only use the following symbols: \n'
              '..... Correct letter, correct position: _\n'
              '... Correct letter, incorrect position: ?\n'
              '..................... Incorrect letter: *')

    if not retry:
        if '*' in symbols:
            indices = [i for i, s in enumerate(symbols) if s == '*']
            for index in indices:
                incorrect_letters.append(letters[index])

        if '?' in symbols:
            indices = [i for i, s in enumerate(symbols) if s == '?']
            for index in indices:
                incorrect_positions[index].append(letters[index])

        if '_' in symbols:
            indices = [i for i, s in enumerate(symbols) if s == '_']
            for index in indices:
                final_word[index] = letters[index]

        if '_' not in ''.join(final_word):
            print('You won!')
            break

        simple_words = list(filter(lambda w: suggestWord(w), simple))

        advanced_words = list(filter(lambda w: suggestWord(w), advanced))

        output = ''.join(final_word)

        print(output.upper())
        print('Simple words:', simple_words)
        print('Advanced words:', advanced_words)
