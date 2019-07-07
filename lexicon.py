# take user input and scan

lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "IAS": 'error',
    "ASDFASDFASDF": 'error',
    "1234": 'number',
    3: 'number',
    91234: 'number'
}

def scan(sentence):
    result = []
    words = sentence.split()
    for word in words:
        check_string = convert_numbers(word) # needed to convert a string to an integer if needed

        if word in lexicon:
            # check if int or return string
            check_number = convert_numbers(word)

            pair = (lexicon[word], check_number)
            result.append(pair)

        elif type(check_string) == type(1): # check if the type of string is an int

            number = convert_numbers(word)

            if number:

                pair = ('number', number)
                result.append(pair)

        else:
            # the tricky part if missing from dict
            error_word = word
            pair = ('error', error_word)
            result.append(pair)

        # word_type = lexicon.get(word)
        # results.append((word_type, word))
    return result

# check if a string can be returned as an int, otherwise as string
def convert_numbers(s):

    try:
        return int(s)
    except ValueError:
        return s
