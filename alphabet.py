# alphabet is a module for natural language processing and machine learning.

from nltk_utils import tf_idf, lemmatize, tokenize
import numpy, spacy, nltk, math

nlp = spacy.load('en_core_web_md')

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

# Calculate the cosine similarity
def CalcCosine(sentence, pattern):
    # https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
    def CosSimilarity(x, y):
        def squared_sum(x):
            return round(math.sqrt(sum([a * a for a in x])), 3)

        numerator = sum(a * b for a, b in zip(x, y))
        denominator = squared_sum(x) * squared_sum(y)
        return round(numerator / float(denominator), 3)

    sentences = [sentence, pattern]
    sentences = [sent.lower() for sent in sentences]
    sentences = [" ".join(tf_idf(i)) for i in sentences]
    sentences = [" ".join(lemmatize(i)) for i in sentences]
    embeddings = [nlp(sentence).vector for sentence in sentences]
    return CosSimilarity(embeddings[0], embeddings[1])

# Classify intentions
def ClassifyIntent(sentence, patterns):
    taglist = [CalcCosine(sentence, pattern) for pattern in patterns]
    SortedScore = [SentScore for SentScore in sorted(taglist, reverse=True)]
    return SortedScore[0]

# Classify whether a sentence is a question or not
def isQuestion(sentence):
    posts = nltk.corpus.nps_chat.xml_posts()[:10000]

    # https://stackoverflow.com/a/50583762/18121288
    def dialogue_act_features(post):
        features = {}
        for word in tokenize(post): features['contains({})'.format(word.lower())] = True
        return features

    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    return "Question" in classifier.classify(dialogue_act_features(sentence))
