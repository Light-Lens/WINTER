import sys
sys.path.append("..")

from w2 import w2

with open("..\\..\\assets\\API.txt") as f: API = f.read()
with open("..\\..\\assets\\chatlog.txt") as f: prompt = f.read()

agent = w2(API)
agent.initalize()
agent.prompt = prompt

# Chat with WINTER
def Chat(text):
    ans = agent.get_response(text)
    with open("assets\\chatlog.txt", "w") as f: f.write(agent.prompt)

    return ans
