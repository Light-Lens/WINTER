# WINTER — (Witty Intelligence with Natural Emotions and Rationality)
WINTER is an AI system built using a combination of Natural Language Processing (NLP), Machine Learning (ML), and Reinforcement Learning (RL) technologies. It is designed to assist users with a variety of tasks, ranging from simple tasks such as setting reminders and scheduling appointments to more complex tasks such as managing emails and organizing data.

One of the key features of WINTER is its ability to understand and respond to natural language inputs, allowing users to interact with it in a way that feels natural and intuitive. This makes it easy for users to communicate with WINTER and ask it to perform tasks or provide information.

In addition to its natural language capabilities, WINTER is also able to learn and adapt to the preferences and habits of its users over time. This allows it to become more efficient at completing tasks and providing relevant information, ultimately making the life of the user easier and more comfortable.

Overall, WINTER is a powerful and intelligent AI system that has the potential to revolutionize the way we interact with technology and automate a variety of daily tasks. Its combination of NLP, ML, and RL technologies make it a versatile and adaptable system that is capable of handling a wide range of tasks and requests. So, it is like Tony Stark's JARVIS.

## Demo
```console
WINTER
```
```
~> WINTER, You up?
For you sir, always.

~> Start a new project indexed as mark 5
Sure.
Shall I store it on your GitHub sir?

~> Yeah sure
Project initalize, shall we start?
```

## The Plan
Plan for Implementing WINTER (Witty Intelligence with Natural Emotions and Rationality)

Identify the specific tasks and responsibilities that WINTER will be responsible for. This may include tasks such as scheduling appointments, sending reminders, managing emails, and organizing data.

Develop a natural language processing (NLP) system that allows WINTER to understand and respond to requests and commands made in natural language. This may involve training the system on a large dataset of natural language inputs and responses.

Implement machine learning (ML) algorithms that allow WINTER to learn and adapt to the preferences and habits of its users over time. This will allow it to become more efficient at completing tasks and providing relevant information.

Integrate reinforcement learning (RL) techniques that allow WINTER to learn from its own experiences and make decisions based on past outcomes. This will allow it to continually improve its performance and become more effective at completing tasks.

## Getting Started
Visual Studio Code is recommended, WINTER is officially untested on other development environments whilst we focus on a Windows build.

Start by cloning the repository with `git clone https://github.com/Light-Lens/WINTER.git`

## Installation
### Requirments
You need to install the following on your machine.
- Visual Studio Code
- Python 3

### Create an environment and Activate it
Whatever you prefer (e.g. conda or venv)
```console
cd WINTER
$ python -m venv venv
$ WINTER\Scripts\activate
```

### Install dependencies
 ```console
$ pip install -r requirements.txt
 ```

If you get an error during the first run, you also need to install `nltk` utils:
Run this once in your terminal:
```console
$ python
```
```python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> nltk.download('omw-1.4')
>>> nltk.download('nps_chat')
>>> nltk.download('stopwords')
```

## Usage
From [main.py](main.py), run
```python
train_all()
```

This will dump `data.pth`, `and.pth`, `nlp.pth` file in [`models`](models) directory. And then run
```console
$ python main.py
```

## Customize
Have a look at [intents.json](models/intents.json). You can customize it according to your own use case. Just define a new `tag`, and possible `patterns` for the system. You have to re-run the training whenever this file is modified.
```json
{
    "intents": [
        {
            "tag": "default",
            "patterns": [""]
        }
    ],
    "and": [
        {
            "tag": "true",
            "patterns": [""]
        },
        {
            "tag": "false",
            "patterns": [""]
        }
    ],
    "nlp": [
        {
            "tag": "true",
            "patterns": [""]
        },
        {
            "tag": "false",
            "patterns": [""]
        }
    ]
}
```

## Acknowledgements
This project is inspired from Tony Stark's JARVIS, and the following videos helped me to make this possible.

[Building JARVIS - Huw Prosser](https://youtube.com/playlist?list=PLMN3MpL-Rb0APuaKJdORgiIWY9vzeHrcp)<br>
[Chat Bot With PyTorch - Patrick Loeber](https://youtube.com/playlist?list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg)<br>
[My J.A.R.V.I.S. Program Quick Demo - Kartikey Sankhdher](https://youtu.be/OCxL-V2Zt8A)<br>
[Iron Man Jarvis AI Desktop Voice Assistant - CodeWithHarry](https://youtu.be/Lp9Ftuq2sVI)<br>

## License and Contributions
All code is licensed under a MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.

We welcome any contributions to WINTER's development through pull requests on GitHub. Most of our active development is in the master branch, so we prefer to take pull requests there (particularly for new features).
