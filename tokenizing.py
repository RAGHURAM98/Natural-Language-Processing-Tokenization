import re
import numpy as np
import nltk
from PyDictionary import PyDictionary as dictionary

try:
    from nltk.corpus import stopwords
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'
    #nltk.download(stopwords)

def get_tokens():
    file = open("sample2.txt","r")
    tokens=file.read().lower()
    tokens = re.sub('[^a-z]', ' ', tokens)
    tokens = nltk.word_tokenize(tokens)
    return tokens

#getting the stopwords from the data
def get_stopwords(data):
    stopword = [w for w in data if w in stopwords.words('english')]
    return stopword

#getting the filtered data by removing stop words
def filtered(data):
    filters = [w for w in data if not w in stopwords.words('english')]
    return filters

#tagging the filtered data into nouns, verbs, adverbs, adjectives
def grammar(tagged):
    nouns=[]
    verbs=[]
    adverbs=[]
    adjectives=[]
    tag=np.array(tagged)
    x,y=tag.T
    for i in range(0,len(x)):
        if (y[i] == 'NN'):
            nouns.append(x[i])
        elif (y[i] == 'JJ'):
            adjectives.append(x[i])
        elif (y[i] == 'VBD'):
            verbs.append(x[i])
        else:
            adverbs.append(x[i])

#getting synonyms from data using pypidictionary
def get_synonyms(adjectives):
    for i in range(0,len(adjectives)):
        print ("synonyms of adjective : %s = %s" %(adjectives[i],dictionary.synonym(adjectives[i])))

# getting anonyms from data using pypidictionary
def get_antonym(adjectives):
    for i in range(0,len(adjectives)):
        print ("antonyms of adjective : %s = %s" %(adjectives[i],dictionary.antonym(adjectives[i])))        

#main function
if __name__ == "__main__":
    tokens = get_tokens()
    stopword=get_stopwords(tokens)
    tokens = filtered(tokens)
    tagged = nltk.pos_tag(tokens)
    [nouns,adjectives,verbs,adverbs]=grammar(tagged)
    get_synonyms(adjectives)
    get_antonym(adjectives)
