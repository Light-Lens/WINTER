import pyjokes

# Tell some joke
def CrackJokes():
    return pyjokes.get_joke(language="en", category="all")
