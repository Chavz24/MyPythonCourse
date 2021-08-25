"""Challenge: Wax Poetic 9.5"""
# creates a 'poem'

from random import choice

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
         "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
         "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant",
              "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon",
                "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly",
           "furiously", "sensuously"]


def non_repeat(lis, n):
    """Makes sure that a word is not repeated in the list"""
    word_list = []
    for i in range(n):
        word = choice(lis)
        if word in word_list:
            while word in word_list:
                word = choice(lis)
            word_list.append(word)
        else:
            word_list.append(word)
    return word_list


def a_or_an(word, start=None):
    """Writes a or an depending if the next word starts or not with a vowel and also
    if you pass the start=1 keyword it writes A or An"""
    if word.startswith(('a', 'e', 'i', 'o', 'u')) and start == 1:
        return f'An {word} '
    elif word.startswith(('a', 'e', 'i', 'o', 'u')):
        return f'an {word} '
    elif start == 1:
        return f'A {word} '
    else:
        return f'a {word} '


noun = non_repeat(nouns, 3)
verb = non_repeat(verbs, 3)
adj = non_repeat(adjectives, 3)
prep = non_repeat(prepositions, 2)
adv = non_repeat(adverbs, 1)

# {A/An} {adj1} {noun1}
# {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
# {adverb1}, the {noun1} {verb2}
# the {noun2} {verb3} {prep2} a {adj3} {noun3}

print(f'{a_or_an(adj[0], start=1)} {noun[0]}.\n')
print(f'{a_or_an(adj[0], start=1)}{noun[0]} {verb[0]} {prep[0]} the {adj[1]} {noun[1]}')
print(f'{adv[0]} the {noun[0]} {verb[1]}')
print(f'the {noun[1]} {verb[2]} {prep[1]} {a_or_an(adj[2])}{noun[2]}.')
