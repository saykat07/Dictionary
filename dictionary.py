import json
info = json.load(open("data.json"))


def dictionary(word):
    word = word.lower()
    if word in info:
        return info[word]
    elif word.title() in info:
        return info[word.title()]
    elif word.upper() in info:
        return info[word.upper()]

    else:
        print("You have put a wrong word.Try Again!")


word = input("What do you want to search: ")
output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)
