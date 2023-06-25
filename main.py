import pandas as pd


def solver():
    """
    This function takes in the center letter and the surrounding letters and returns the words that can be made from
    those letters. It also returns the top ten words by word length and the perfect words that can be made from the
    letters.
    """
    main_letter = input('What is the center letter? ')

    all_letters = main_letter + input('What are the surrounding letters? Enter them together as in "abcdef" ')

    non_letters = list('abcdefghijklmnopqrstuvwxyz')  # create a list of string characters from a to z
    for letter in all_letters:
        non_letters.remove(letter)

    words = pd.read_csv('word_list.csv').rename(columns={'a': 'word'}).drop_duplicates()  # read in the word list

    words = words.loc[words['word'].str.len() >= 5]  # only words with 5 or more letters

    words = words[words['word'].str.contains(main_letter)]  # only words with the main letter

    words = words[words['word'].str.match('^[' + all_letters + ']+$')]  # only words with the letters in the puzzle

    words['word length'] = words['word'].str.len()  # add a column for word length

    words = words.sort_values(by=['word length'], ascending=False)  # sort by word length

    # create a list of perfect words
    perfect_words = words.copy()
    for letter in all_letters:
        perfect_words = perfect_words[perfect_words['word'].str.contains(letter)]
    for letter in non_letters:
        perfect_words = perfect_words[~perfect_words['word'].str.contains(letter)]

    print('\nThere are ' + str(words.shape[0]) + ' words for this puzzle.\n')

    print('The perfect words are: ')

    i = 1
    for word in list(perfect_words['word']):
        print(str(i) + '.  ' + word)
        i = i + 1

    print('\nThe top ten words by word length are: ')

    i = 1
    for word in list(words['word'])[0: 9]:
        print(str(i) + '.  ' + word)
        i = i + 1
    print(str(i) + '. ' + list(words['word'])[9])

    words.to_csv('words_result.csv', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solver()
