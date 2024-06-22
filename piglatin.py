print('Enter the english message to be translated to piglatin:')
message = input()

VOWELS = ('a','i','e','o','u','y')

pigLatin = [] # a list of words in pig Latin

for word in message.split():
    # separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    print(prefixNonLetters)
 
    # separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    # remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower() # make the word lowercase for translation.
    
    # separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    
    # add the pig latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    
    # join all the words back together into a single string:
    print(' '.join(pigLatin))