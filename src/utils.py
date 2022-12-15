import numpy, spacy, nltk, math

from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
Lemmatizer = WordNetLemmatizer()

nlp = spacy.load('en_core_web_md')

def nGrams(words, ngram): return ngrams(words, ngram)

def tokenize(sentence): return nltk.word_tokenize(sentence)
def sent_tokenize(sentence): return nltk.sent_tokenize(sentence)

def stem(word): return stemmer.stem(word.lower())
def lemmatize(word): return Lemmatizer.lemmatize(word.lower())

def bag_of_words(tokenized_sentence, words):
    sentence_words = [lemmatize(word) for word in tokenized_sentence]

    bag = numpy.zeros(len(words), dtype=numpy.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:  bag[idx] = 1

    return bag

# Calculate the cosine similarity
def CalcCosine(sentence, pattern):
    # https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
    squared_sum = lambda x : round(math.sqrt(sum([a * a for a in x])), 3)
    stop_words = set(stopwords.words("english"))

    # Clean the sentence and pattern text
    tok1 = tokenize(sentence.lower())
    tok2 = tokenize(pattern.lower())

    clean_tok1 = [word for word in tok1 if word not in stop_words]
    clean_tok2 = [word for word in tok2 if word not in stop_words]

    clean_sentence = " ".join([lemmatize(word) for word in clean_tok1])
    clean_pattern = " ".join([lemmatize(word) for word in clean_tok2])

    # Create vectors of the given sentence and pattern
    vec1 = nlp(clean_sentence).vector
    vec2 = nlp(clean_pattern).vector

    # Calc the cosine similarity
    numerator = sum(a * b for a, b in zip(vec1, vec2))
    denominator = squared_sum(vec1) * squared_sum(vec2)
    return 0.0 if not float(denominator) else round(numerator / float(denominator), 3)

# Classify intentions
def ClassifyIntent(sentence, patterns):
    return max([[CalcCosine(sentence.lower(), pattern.lower()), pattern] for pattern in patterns])

# Arrange words in such a way to form a logical sentence.
def ArrangeWords(Words):
    # A number will represent the number of empty strings in a list.
    # For example: 4 -> ["", "", "", ""].
    for i in Words:
        for j in i:
            if isinstance(j, int):
                EmptyList = [""] * j
                i.extend(EmptyList)
                i.remove(j)
                break

    GreetingSentence = [numpy.random.choice(i) for i in Words]

    # Reconstruct the string to form a logical sentence.
    FinalSentence = " ".join(GreetingSentence)
    rm_extra_spaces = " ".join(FinalSentence.split())
    return rm_extra_spaces
