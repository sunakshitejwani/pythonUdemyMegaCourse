import json
data = json.load(opne("data.json"))

def translate(word):
	return data[word]

word = input("Enter word:")
print(translate(word))
