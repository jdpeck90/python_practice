import json

from difflib import SequenceMatcher, get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        responseToWordRatio = input(
            "Did you mean %s instead? Enter Y if yes, or N if no:  " % get_close_matches(w, data.keys())[0])
        if responseToWordRatio == "Y":
            x = get_close_matches(w, data.keys())[0].capitalize()
            y = " is "
            z = data[get_close_matches(w, data.keys())[0]][0]
            zz = "%s%s%s" % (x, y, z)
            return zz
        elif responseToWordRatio == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check input."


word = input("enter word: ")


output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
