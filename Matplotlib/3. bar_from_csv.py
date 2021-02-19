# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
languages_used = data['LanguagesWorkedWith']

language_counter = Counter()

for language in languages_used:
    language_counter.update(language.split(';'))
    
#print(language_counter)

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
    
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('Number of People Who use')
plt.ylabel('Programming languages')

plt.show()