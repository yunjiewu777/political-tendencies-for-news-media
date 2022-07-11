import pickle

import json
import math
import requests
from nltk import tokenize
import numpy as np

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')


API_URL = "https://api-inference.huggingface.co/models/yangheng/deberta-v3-base-absa-v1.1"
headers = {"Authorization": f"Bearer {'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'}"}


def sentiment(sentence_list):
    result = []
    for subtopic in topic:
        a = dict()
        b = dict()
        for word in subtopic:
            a[word] = np.array([0, 0, 0])
            b[word] = 0
            for sentence in sentence_list:
                if contains_word(sentence, word):
                    q = {"inputs": "[CLS] " + sentence + " [SEP] " + word + " [SEP]"}
                    print(sentence)
                    output = query(q)
                    b[word] = b[word] + 1
                    print(word)
                    a[word] = a[word] + np.array([output[0][0]['score'], output[0][1]['score'], output[0][2]['score']])
        sum = np.array([0, 0, 0])
        for word in subtopic:
            if b[word] != 0:
                sum = sum + (subtopic[word] * a[word]) / b[word]
        result.append(sum)
    return result


def sentiment_imp(sentence_list):
    result = []
    all_word = set()
    for subtopic in topic:
        for word in subtopic:
            all_word.add(word)

    a = dict()
    b = dict()
    for word in all_word:
        a[word] = np.array([0, 0, 0])
        b[word] = 0
        for sentence in sentence_list:
            if contains_word(sentence, word):
                q = {"inputs": "[CLS] " + sentence + " [SEP] " + word + " [SEP]"}
                output = query(q)
                print(word)
                b[word] = b[word] + 1
                a[word] = a[word] + np.array([output[0][0]['score'], output[0][1]['score'], output[0][2]['score']])
    c = dict()
    for word in all_word:
        if b[word] != 0:
            c[word] = a[word] / b[word]

    for subtopic in topic:
        sum = np.array([0, 0, 0])
        for word in subtopic:
            if word in c:
                sum = sum + subtopic[word] * c[word]
        result.append(sum)
    return result


q = {"inputs": "[CLS] What's wrong with you? [SEP] you [SEP]"}
print(query(q))

with open("../res/final/co_V.json") as input_file:
    co = json.load(input_file)
with open("..//res/subtopic/covid.json") as input_file:
    topic = json.load(input_file)

result = []
sum = 1
for article in co:
    paragraph = article['content'].lower()
    sentence_list = tokenize.sent_tokenize(paragraph)
    tem = sentiment_imp(sentence_list)
    print(article['source'], tem)
    print(sum)
    sum = sum + 1
    result.append(tem)

with open("../res/final/co_Vox", "wb") as fp:  # Pickling
    pickle.dump(result, fp)

print('done')