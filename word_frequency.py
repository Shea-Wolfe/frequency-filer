import re

def word_frequency(text):
    trim_text = re.sub(r'[^a-zA-Z0-9\s]','' ,text).lower()
    word_list = trim_text.split()
    word_count = {}
    for word in word_list:
        word_count[word] =  word_list.count(word)
    return word_count
def main():
    text = open('sample.txt')
    read_text = text.read()
    word_count = word_frequency(read_text)
    word_count = sorted(word_count.items(), key=lambda c: c[1], reverse=True)
    word_count = word_count[:20]
    for pair in word_count:
        print(pair)
    text.close()

if __name__ == '__main__':
    main()
