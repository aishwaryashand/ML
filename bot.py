import nltk
from nltk.chat.util import Chat, reflections

'''pairs = [
    [
        r'hi',
        ['hello', 'kamusta', 'mabuhay',]
    ],
]'''

pairs = [
    [
        r"My name is (.*)",
        ['hello %1',]
    ],
    [
        r'hi',
        ['hello', 'kamusta',]
    ],
    [
        r'how are you',
        ['I\'m fine', 'tell me about you?']
    ],
]

def gusto_bot():
    print("Hi how can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    gusto_bot()


