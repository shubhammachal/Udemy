import json,difflib
from difflib import SequenceMatcher
data = json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif SequenceMatcher(None,w,word).ratio > 0.8:
        return data[w]
    else:
        return "The word doesn't exists"
    return data[w]
word = input("Enter the word in double quotes: ")
print(translate(word))
