import numpy, time

# dprint -> delay print
# ChatGPT like print effect.
def dprint(text, delay=0.001):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Arrange words in such a way to form a logical sentence.
def arrange_words(tokens):
    """
    A number will represent the number of empty strings in a list.
    For example: 4 -> ["", "", "", ""].
    """

    processed_tokens = []
    for sublist in tokens:
        if isinstance(sublist[-1], int):
            empty_list = [""] * sublist[-1]
            processed_tokens.append(sublist[:-1] + empty_list)

        else:
            processed_tokens.append(sublist)

    # Construct a logical sentence.
    sentence = [numpy.random.choice(i) for i in processed_tokens]
    return " ".join(sentence)
