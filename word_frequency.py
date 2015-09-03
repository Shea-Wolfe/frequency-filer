import re
test = 'This, is a Sample. Paragraph, for. some, basic testing yes yes yes yes yes.'

def word_frequency(text):
    trim_text = re.sub(r'[^a-zA-Z0-9\s]','' ,text).lower()
    word_list = trim_text.split()
    word_count = {}
    for word in word_list:
        word_count[word] =  word_list.count(word)
    return print(word_count)
word_frequency(test)
