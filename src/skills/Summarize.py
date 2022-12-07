import sys
sys.path.append("..")

import wikipedia, heapq, re

from src.nltk_utils import tokenize, sent_tokenize
from nltk.corpus import stopwords

# Summarize any text
def Summarize(Query):
    try:
        article_text = wikipedia.summary(Query.lower(), sentences=5)

        # Removing Square Brackets and Extra Spaces
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        # Removing special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

        sentence_list = sent_tokenize(article_text)
        stop_words = stopwords.words('english')

        word_frequencies = {}
        for word in tokenize(formatted_article_text):
            if word not in stop_words:
                if word not in word_frequencies.keys(): word_frequencies[word] = 1
                else: word_frequencies[word] += 1

        maximum_frequncy = max(word_frequencies.values())
        for word in word_frequencies.keys(): word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

        sentence_scores = {}
        for sent in sentence_list:
            for word in tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys(): sentence_scores[sent] = word_frequencies[word]
                        else: sentence_scores[sent] += word_frequencies[word]

        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)

        return summary

    except Exception as e: return None
