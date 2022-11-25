import numpy, spacy, nltk, math
from operator import itemgetter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
Lemmatizer = WordNetLemmatizer()
nlp = spacy.load('en_core_web_md')

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

def tf_idf(sentence):
    stop_words = set(stopwords.words('english'))
    total_words = sentence.split()
    total_word_length = len(total_words)

    total_sentences = sent_tokenize(sentence)
    total_sent_len = len(total_sentences)

    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())

    def check_sent(word, sentences):
        final = [all([w in x for w in word]) for x in sentences]
        sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
        return int(len(sent_len))

    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

    def get_top_n(dict_elem, n=None):
        result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n])
        return result

    return list(get_top_n(tf_idf_score).keys())

# lemmatize sentences
def lemmatize(word):
    # stop_words = set(stopwords.words("english"))
    # tokens = tokenize(sentence.lower())

    # TokenizeWordsWithoutStopwords = [word for word in tokens if word not in stop_words]
    # return [Lemmatizer.lemmatize(word) for word in TokenizeWordsWithoutStopwords]
    return Lemmatizer.lemmatize(word.lower())

def extract_ne(quote):
    words = tokenize(quote)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE")

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
