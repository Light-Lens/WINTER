import time

# dprint -> delay print
# ChatGPT like print effect.
def dprint(text, delay=0.001):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
