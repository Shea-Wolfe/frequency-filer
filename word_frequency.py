import re #used to strip non-text

def word_frequency(text):
    '''takes a string and returns a dictionary of {word:count_of_word}'''
    trim_text = re.sub(r'[^a-zA-Z\s]','' ,text).lower()
    #trim_text is the string without formating or numbers but with spaces
    word_list = trim_text.split()
    #word_list splits the string into a list words
    word_count = {} #a dictionary to put our counts in
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
            #optimized so that we don't have to count our entire
            #file on every step.  Speeds up call speed by a lot.
        else:
            word_count[word] = 1
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
