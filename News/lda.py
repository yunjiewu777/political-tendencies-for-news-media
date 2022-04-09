import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(400)
import json
import nltk
import pandas as pd
import random
import pickle
import pyLDAvis
import gensim.corpora as corpora

stemmer = SnowballStemmer("english")
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


# Tokenize and lemmatize
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))

    return result

if __name__ == '__main__':
    with open("../res/immigration.json") as input_file:
        random_gun = json.load(input_file)
    test = dict()
    for i in random_gun:
        if (i['source'] in ['National Review','CNN (Web News)', 'New York Times - News', 'Fox News', 'USA TODAY']):
            test.setdefault(i['source'],[]).append(i)


    processed_docs = []

    for doc in random_gun:
        processed_docs.append(preprocess(doc['content']))

    dictionary = gensim.corpora.Dictionary(processed_docs)
    bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

    document_num = 20
    bow_doc_x = bow_corpus[document_num]
    lda_model =  gensim.models.LdaMulticore(bow_corpus,
                                       num_topics = 4,
                                       id2word = dictionary,
                                       passes = 10,
                                       workers = 2)

#    for idx, topic in lda_model.print_topics(-1):
#        print("Topic: {} \nWords: {}".format(idx, topic ))
#       print("\n")

    topic = dict()

    for i in ['National Review', 'CNN (Web News)', 'New York Times - News', 'Fox News', 'USA TODAY']:
        for news in test[i]:
            bow_vector = dictionary.doc2bow(preprocess(news['content']))
            topic.setdefault(i, []).append([lda_model[bow_vector][0][0],news['content']])
            print(i,lda_model[bow_vector][0][0],news['content'])



    with open('test.pkl', 'wb') as f:
        pickle.dump(topic, f)


 #   for i in ['National Review', 'CNN (Web News)', 'New York Times - News', 'Fox News', 'USA TODAY']:
        #for news in topic[i]:
            # print(i,news)


    for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1]):
        print("Score: {}\t Topic: {}".format(score, lda_model.print_topic(index, 5)))


    bow_vector = dictionary.doc2bow(preprocess("Federal law allows people 18 and older to legally purchase long guns , including this kind of assault weapon"))


    # Term Document Frequency
    corpus = [dictionary.doc2bow(text) for text in processed_docs]

    # Visualize the topics
    LDAvis_prepared = pyLDAvis.prepare(lda_model, term_frequency=corpus, vocab=dictionary)
    print(LDAvis_prepared)
    