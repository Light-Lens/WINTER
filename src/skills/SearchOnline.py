import pywhatkit, wikipedia

# Search on Google or Wikipedia.
def SearchOnline(Query):
    try:
        pywhatkit.search(Query)
        return wikipedia.summary(Query, sentences=2)

    except Exception as e: return ""
