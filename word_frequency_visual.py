from itertools import count
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.style.use('ggplot')

import numpy as np


from most_common_words_all_books import count_words
from most_common_words_all_books import filename_1

count_words(filename_1)

plt.bar(list(count_words(filename_1).keys()), count_words(filename_1).values(), color='purple')
plt.title("Occurrences of the 20 most common words in 'Alice's Adventures in Wonderland'", fontsize = 20)
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.show()


