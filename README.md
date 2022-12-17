# WINTER — (Witty Intelligence with Natural Emotions and Rationality)
WINTER in particular is an AI program that is designed to help users gain a better understanding of the language they use by providing contextual information to the words they enter. It is built upon concepts like natural language processing (NLP), machine learning (ML), and reinforcement learning (RL), which are all used to create such a comprehensive system.

## Getting Started
Visual Studio Code is recommended, WINTER is officially untested on other development environments whilst we focus on a Windows build.

Start by cloning the repository with `git clone https://github.com/Light-Lens/WINTER.git`

## The Plan
The plan for WINTER is to create a Powerful, General Purpose, AI system which can assist you with a variety of tasks.

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
pip install -r requirements.txt
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
Run from `main.py`
```python
train_all()
```

This will dump `data.pth`, `and.pth`, `nlp.pth` file in [`models`](models) directory. And then run
```console
python main.py
```

## Customize
Have a look at [intents.json](models/intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the system. You have to re-run the training whenever this file is modified.
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

[My J.A.R.V.I.S. Program Quick Demo - Kartikey Sankhdher](https://youtu.be/OCxL-V2Zt8A)
[Iron Man Jarvis AI Desktop Voice Assistant - CodeWithHarry](https://youtu.be/Lp9Ftuq2sVI)


[Building JARVIS - Huw Prosser](https://youtube.com/playlist?list=PLMN3MpL-Rb0APuaKJdORgiIWY9vzeHrcp)
[Chat Bot With PyTorch - Patrick Loeber](https://youtube.com/playlist?list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg)

## License and Contributions
All code is licensed under a MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.

We welcome any contributions to WINTER's development through pull requests on GitHub. Most of our active development is in the master branch, so we prefer to take pull requests there (particularly for new features).
