import numpy, spacy, nltk, math

from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
Lemmatizer = WordNetLemmatizer()

nlp = spacy.load('en_core_web_md')
with open("assets\\stopwords.txt") as file:
    stop_words = file.read().split(",")

# nltk.download('punkt')
def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)

def sent_tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.sent_tokenize(sentence)


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = numpy.zeros(len(words), dtype=numpy.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

# lemmatize sentences
def lemmatize(word):
    return Lemmatizer.lemmatize(word.lower())

# Calculate the cosine similarity
def CalcCosine(sentence, pattern):
    # https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
    squared_sum = lambda x : round(math.sqrt(sum([a * a for a in x])), 3)
    stop_words = set(stopwords.words("english"))

    # Remove stopwords and lemmatize the sentence and pattern
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

def nGrams(words, ngram):
    return ngrams(words, ngram)
