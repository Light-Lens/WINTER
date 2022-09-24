# alphabet is a module for natural language processing and machine learning.
from assets.nltk_utils import tf_idf, lemmatize, tokenize
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

# Calculate the cosine similarity
def CalcCosine(sentence, pattern):
    # https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
    def squared_sum(x): return round(math.sqrt(sum([a * a for a in x])), 3)

    sentence = " ".join(lemmatize(sentence))
    pattern = " ".join(lemmatize(pattern))

    sentence = " ".join(tf_idf(sentence))
    pattern = " ".join(tf_idf(pattern))

    vec1 = nlp(sentence).vector
    vec2 = nlp(pattern).vector

    numerator = sum(a * b for a, b in zip(vec1, vec2))
    denominator = squared_sum(vec1) * squared_sum(vec2)
    return 0.0 if not float(denominator) else round(numerator / float(denominator), 3)

# Classify intentions
def ClassifyIntent(sentence, patterns):
    return max([CalcCosine(sentence.lower(), pattern.lower()) for pattern in patterns])
