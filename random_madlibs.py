

def get_nouns():
    nouns = {}
    for i in range(1,4):
        nouns[f"noun{i}"] = input(f"Noun{i}: ")
    return nouns

nouns = get_nouns()


def get_adj():
    adjs = {}
    for i in range(1,4):
        adjs[f"adj{i}"] = input(f"Adjective{i}: ")
    return adjs

adjs = get_adj()


def get_verbs():
    verbs = {}
    for i in range(1,4):
        verbs[f"verb{i}"] = input(f"Verb{i}: ")
    return verbs

verbs = get_verbs()


madlib = f"One {adjs['adj1']} morning, a {nouns['noun1']} met a {adjs['adj2']} {nouns['noun2']} . \
The {nouns['noun1']} decided to {verbs['verb1']}, but the {nouns['noun2']} began to {verbs['verb2']} instead. \
Suddenly, a {adjs['adj3']} {nouns['noun3']} appeared and started to {verbs['verb3']} loudly. \
The {nouns['noun1']}, the {nouns['noun2']}, and the {nouns['noun3']} all looked at each other. \
Then the {adjs['adj1']} {nouns['noun1']} tried to {verbs['verb2']}, the {adjs['adj2']} {nouns['noun2']} tried to {verbs['verb3']}, \
and the {adjs['adj3']} {nouns['noun3']} decided to {verbs['verb1']}. \
Nobody knows why they did that … but it was definitely a {adjs['adj1']} day."

print(madlib)