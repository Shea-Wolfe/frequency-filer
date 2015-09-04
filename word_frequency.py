import re #used to strip non-text

def word_frequency(text):
    '''takes a string and returns a dictionary of {word:count_of_word}'''
    trim_text = re.sub(r'[^a-zA-Z\s]','' ,text).lower()
    #trim_text is the string without formating or numbers but with spaces
    word_list = trim_text.split()
    #word_list splits the string into a list words
    word_count = {} #a dictionary to put our counts in
    for word in word_list:
        word_count[word] =  word_list.count(word)
        #looks at every word in our list and sets it as
        #a key with a value equal to the count of that word
        #in the the list.  duplicates are overwritten.
    return word_count

def sorted_frequency(dictionary):
    word_count = sorted(dictionary.items(), key=lambda c: c[1], reverse=True)
    #returns a list of our key-value pairings (.items creates tuples of our key-item pairing)
    #sorted by values (higher to lower due to reverse)
    word_count = word_count[:20] #cuts off the top 20 most frequent words
    for pair in word_count:
        print(pair)
        #Iterates through our list and prints out each tuple on it's own line

def main():
    text = open('sample.txt') #opens the outside file
    read_text = text.read() #reads the text file
    word_count = word_frequency(read_text) #runs the count function on the file
    sorted_frequency(word_count) #sorts the dictionary by count and prints the top 20 to stdout
    text.close() #closes the outside file

if __name__ == '__main__':
    main()
