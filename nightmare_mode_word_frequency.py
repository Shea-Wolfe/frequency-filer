import re
import sys #sys found on stack overflow

def word_frequency(text):
    trim_text = re.sub(r'[^a-zA-Z\s]','' ,text).lower()
    #trim_text is the string without formating or numbers but with spaces
    del_words = ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be',
'because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every',
'for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is',
'it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor',
'not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should',
'since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too',
'twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with',
'would','yet','you','your'] #can be any list of strings
    word_list = trim_text.split()
    #word_list splits the string into a list words
    word_count = {} #a dictionary to put our counts in
    for word in word_list:
        word_count[word] =  word_list.count(word)
        #looks at every word in our list and sets it as
        #a key with a value equal to the count of that word
        #in the the list.  duplicates are overwritten.
    for word in del_words:
        try:
            del word_count[word]
        except:
            pass
        #iterates through our library and deletes any key that appears in our del_list
    return word_count

def sorted_frequency(dictionary):
    word_count = sorted(dictionary.items(), key=lambda c: c[1], reverse=True)
    #returns a list of our key-value pairings (.items creates tuples of our key-item pairing)
    #sorted by values (higher to lower due to reverse)
    word_count = word_count[:20] #cuts off the top 20 most frequent words
    if word_count[0][1] > 50:
        ratio = 50/int(word_count[0][1])
        #We set the cap at 50 and scale everything relatively
        #Since we aren't set up for partial #'s we just truncate with int()
        for pair in word_count:
            word, count = pair[0], pair[1] #unpack the tuple
            new_pairs = (word, '#'*(int(count*ratio)))
            #creates a new tuple with #'s equal to the proportion of the current
            #item's count when the largest count is scaled down to 50.
            print(new_pairs)
    else:
        for pair in word_count:
            word, count = pair[0], pair[1]
            new_pairs = (word, '#'*int(count))
            #Since we aren't scaling down we can just print #'s equal to the count.
            print(new_pairs)
        #Iterates through our list and prints out each tuple on it's own line
def main():
    input_file = sys.argv[1] #sys and sys.argv found on stack overflow
    text = open(input_file) #opens the file
    read_text = text.read() #reads the text file
    word_count = word_frequency(read_text) #runs the count function on the file
    sorted_frequency(word_count) #sorts the dictionary by count and prints the top 20 to stdout
    text.close() #closes the outside file


if __name__ == '__main__':
    main()
