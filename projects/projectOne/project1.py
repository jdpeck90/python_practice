import json

from difflib import SequenceMatcher, get_close_matches


data = json.load(open("data.json"))


def translate(w):
    print("before", w)
    w = w.lower()
    print("after", w)
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:

        return "The word doesn't exist. Please double check input."


word = input("enter word: ")


print(translate(word))
