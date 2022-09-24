# WINTER
WINTER (Witty Intelligence with Natural Emotions and Rationality) is an artificially intelligent system inspired by JARVIS from the Iron man movies.

## Getting Started
Visual Studio Code is recommended, WINTER is officially untested on other development environments whilst we focus on a Windows build.

Start by cloning the repository with `git clone https://github.com/Light-Lens/WINTER.git`.

## The Plan
The plan for WINTER is to create a Powerful, General Purpose, AI system which can assist you with a variety of tasks, 24 hours a day, 7 days a week.

## Demo
```console
WINTER
```
```
~> Wake up
Online and ready!

~> Hello
Namaste :)

~> How are you?
I am doing a bit better than before, but not nearly as awesome as I am going to be.

~> What are you doing?
Existing.
What are you doing?

~> Nothing, just talking to you.
Hmmm

~> Do you know what is life?
I think, therefore I am.

~> Impressive!
I know, right.
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
$ python3 -m venv WINTER
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
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> nltk.download('nps_chat')
>>> nltk.download('stopwords')
```

## Usage
Run
```console
train.bat
```

This will dump `data.pth` file in `.\data\models` directory. And then run
```console
python main.py
```

## Customize
Have a look at [intents.json](data/models/intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the system. You have to re-run the training whenever this file is modified.
```console
{
    "intents": [
        {
            "tag": "say hello",
            "patterns": [
                "hello",
                "hi there",
                "hey",
                "namaste"
            ],
            "responses": [
                [
                    "Hello.",
                    "Hi.",
                    "How are you doing.",
                    "Namaste.",
                    "Greetings and salutations.",
                    "What's up with you?",
                    "How are you doing?",
                    "How have you been?"
                ]
            ]
        },
        ...
    ]
}
```

## License and Contributions
All code is licensed under a MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.

We welcome any contributions to WINTER's development through pull requests on GitHub. Most of our active development is in the master branch, so we prefer to take pull requests there (particularly for new features).
