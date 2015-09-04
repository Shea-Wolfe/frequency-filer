## Getting Started
* To run test in command line use $ python word_frequency_test.py.
* To run word_frequency in command line use $ python word_frequency.py.  This program requires a file named sample.txt to be present in the same directory.
* To run hard_word_frequency in command line use $ python hard_word_frequency file_to_be_opened.txt.

## The programs
word_frequency will open an outside file in the same directory named sample.txt and print pairings of the 20 most common words in sample.txt and how many times they are used to standard output.

word_frequency_tests checks the word_frequency() function in word_frequency.py and ensures it is properly counting each word and sorting them into a dictionary where key=word and value=count of that word.

sample.txt is a file to be input into our word_frequency function.

hard_word_frequency will open the text file indicated after you call hard_word_frequency and print out the 20 most common words excluding the words found below.

excluded words:
['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be',
'because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every',
'for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is',
'it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor',
'not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should',
'since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too',
'twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with',
'would','yet','you','your']
