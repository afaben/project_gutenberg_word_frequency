#Program that counts the frequency of each unique word in a book.
"""
Need to first import the book
Automatically generate lists each time a new word appears
if next_word not in list_of_unique_words
Account for non-relevant text so where it says END OF THE PROJECT GUTENBERG EBOOK end program there
Apply regex to remove non-alphabetic characters
Remove text before *** Start of... *** and at end of novel
"""
from itertools import count, dropwhile
import re
from collections import Counter
from typing import OrderedDict

def count_words(filename):
    """Counts the number of unique words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Error: File does not exist." + " (" + filename + ")"
        print(msg)
    else:
        """Count the unique number of words in the file."""
        #Turns the text file into list containing each word as a string
        words_list = contents.split()
        num_words_novel = len(words_list)

        #Convert each item in the list to lower case
        for i in range(len(words_list)):
            words_list[i] = words_list[i].lower()

        #Remove non-alphabetical items in the list
        for i in range(len(words_list)):
            words_list[i] = re.sub(r"[^a-zA-Z]+", '', words_list[i])
            words_list[i] = re.sub(r'[0-9]+', '', words_list[i])
        
        #Remove the blank string replaced from code above
        words_list_no_blank = []
        for single_word in words_list:
            if single_word != '' or 'e' or 'gutenbergtm' or 'gutenberg' or 'trademark' or 'ebook' or 'electronic':
                words_list_no_blank.append(single_word)
        
        #Count occurrences of 20 most common words and stores the K-Vs in tuples
        counted_sorted_words = Counter(words_list_no_blank).most_common(20)
        
        #Converts the list of tuples into a dictionary
        dict_counted = dict(counted_sorted_words)
        return(dict_counted)
        
               
filenames = ['A Christmas Carol.txt', "A Doll's House.txt", 'A Modest Proposal.txt', 'A Tale of Two Cities.txt', "Alice's Adventures in Wonderland.txt", 'Crime and Punishment.txt', 'Dracula.txt',
    'Frankenstein.txt', 'Great Expectations.txt', "Grimm's Fairy Tales.txt", 'Heart of Darkness.txt', 'Jane Eyre.txt', 'Metamorphosis.txt', 'Moby-Dick.txt', 'Pride and Prejudice.txt', 'The Adventures of Sherlock Holmes.txt',
    'The Great Gatsby.txt', 'The Importance of Being Earnest.txt', 'The Picture of Dorian Gray.txt', 'The Prince.txt', 'The Scarlet Letter.txt', 'The Strange Case of Dr Jekyll and Mr Hyde.txt', 'Twas the Night before Christmas.txt',
    ]

filename_1 = "Alice's Adventures in Wonderland.txt"
print(count_words(filename_1))




