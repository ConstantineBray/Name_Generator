import requests
from random import randint

urlAdj = "https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt"
urlNoun = "https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt"

r = requests.get(urlAdj)
textAdj = r.text

r = requests.get(urlNoun)
textNoun = r.text

individual_adjectives = textAdj.split()
individual_nouns = textNoun.split()

random_adjnumber = randint(0, len(individual_adjectives))
random_nounnumber = randint(0, len(individual_nouns))

adjective = individual_adjectives[random_adjnumber].capitalize()
noun = individual_nouns[random_nounnumber].capitalize()


print(adjective + noun + str(random_nounnumber))



