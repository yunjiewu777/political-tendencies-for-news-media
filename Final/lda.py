import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from gensim import corpora, models
from nltk.stem.porter import *
import numpy as np
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis


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
    with open("../res/data/immigration.json") as input_file:        imm = json.load(input_file)

    processed_docs = []

    for doc in imm:
        processed_docs.append(preprocess(doc['content']))

    dictionary = gensim.corpora.Dictionary(processed_docs)
    bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

    # immigration
    del_ids1 = [k for k, v in dictionary.items() if v in ['year','say','peopl','like']]
    # coronavirus
    # del_ids2 = [k for k, v in dictionary.items() if v in ['say','like','go']]
    # healthcare
    #del_ids3 = [k for k, v in dictionary.items() if v in ['say', 'peopl', 'year', 'go']]

    print(del_ids1)
    # print(del_ids2)
    #print(del_ids3)

    gensim.corpora.MmCorpus.serialize('MmCorpusTest.mm', bow_corpus)
    dictionary.filter_tokens(bad_ids=del_ids1)
    corpusMm = gensim.corpora.MmCorpus('MmCorpusTest.mm')
    np_corpus = gensim.matutils.corpus2dense(corpusMm, corpusMm.num_terms, num_docs=corpusMm.num_docs).T
    np_corpus = np.delete(np_corpus, del_ids1, 1).T
    new_corpus = gensim.matutils.Dense2Corpus(np_corpus)

    num_topics = 3
    lda_model = models.LdaModel(new_corpus, num_topics=num_topics,
                                id2word=dictionary,
                                passes=4, alpha=[0.01] * num_topics,
                                eta=[0.01] * len(dictionary.keys()))
    for i, topic in lda_model.show_topics(formatted=True, num_topics=num_topics, num_words=20):
        print(str(i) + ": " + topic)
        print()

    bow_vector = dictionary.doc2bow(preprocess(imm[1]['content']))
    print(lda_model[bow_vector])
    print(imm[1])


    print("------------------------------------------------------------------------------")

    num_topics = 4
    lda_model = models.LdaModel(new_corpus, num_topics=num_topics,
                                id2word=dictionary,
                                passes=4, alpha=[0.01] * num_topics,
                                eta=[0.01] * len(dictionary.keys()))
    for i, topic in lda_model.show_topics(formatted=True, num_topics=num_topics, num_words=20):
        print(str(i) + ": " + topic)
        print()

    print("------------------------------------------------------------------------------")

    num_topics = 5
    lda_model = models.LdaModel(new_corpus, num_topics=num_topics,
                                id2word=dictionary,
                                passes=4, alpha=[0.01] * num_topics,
                                eta=[0.01] * len(dictionary.keys()))
    for i, topic in lda_model.show_topics(formatted=True, num_topics=num_topics, num_words=20):
        print(str(i) + ": " + topic)
        print()

    vis = gensimvis.prepare(topic_model=lda_model, corpus=new_corpus, dictionary=dictionary)
    pyLDAvis.enable_notebook()
    pyLDAvis.display(vis)

"""
    document_num = 20
    bow_doc_x = bow_corpus[document_num]
    lda_model =  gensim.models.LdaMulticore(new_corpus,
                                       num_topics = 4,
                                       id2word = dictionary,
                                       passes = 10,
                                       workers = 2)

    for idx, topic in lda_model.print_topics(-1):
        print("Topic: {} \nWords: {}".format(idx, topic ))
        print("\n")


 #   for i in ['National Review', 'CNN (Web News)', 'New York Times - News', 'Fox News', 'USA TODAY']:
        #for news in topic[i]:
            # print(i,news)


    bow_vector = dictionary.doc2bow(preprocess("Federal law allows people 18 and older to legally purchase long guns , including this kind of assault weapon"))


    # Term Document Frequency
    corpus = [dictionary.doc2bow(text) for text in processed_docs]
 """
