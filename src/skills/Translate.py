from googletrans import Translator

# init modules
translator = Translator()

# Translate to any language
def Translate(sent):
    out = translator.translate(sent, dest="en")
    return out.text
