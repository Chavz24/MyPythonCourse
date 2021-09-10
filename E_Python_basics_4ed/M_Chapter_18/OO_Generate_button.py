"""Challenge: Return of the Poet 18.10"""

import re, random

# The generate button function.

word_regex = re.compile("^[A-Za-z]*$")


def a_or_an(word, start=None):
    """Writes a or an depending if the next word starts or not with a vowel and also
    if you pass the start=1 keyword it writes A or An"""

    if word.startswith(('a', 'e', 'i', 'o', 'u')) and start == 1:
        return f'An {word}'
    elif word.startswith(('a', 'e', 'i', 'o', 'u')):
        return f'an {word}'
    elif start == 1:
        return f'A {word}'
    else:
        return f'a {word}'


def generate_button():
    """This function checks the entries widgets and generate a poem.
        It also checks if the words are repeated ot if there aren't enough words."""

    import OO_Visual_layout_Challenge as layout

    raw_entries = [
        layout.ent_word_noun, layout.ent_word_verb, layout.ent_word_adj,
        layout.ent_word_prep, layout.ent_word_adv
    ]
    clean_entries = []
    error_msj = f"Error:\nYou have to enter " \
                f"\n3 nous, 3 verbs,3 adjectives" \
                f"\n2 prepositions and an adverb."

    for entry_box in raw_entries:
        count_words = entry_box.get().split(",")  # Makes a list of words in the ent_box.
        words = [word.strip(" ") for word in count_words]  # Makes a list of the words without spaces.

        # Checks for duplicated words in an entry box.

        for word in words:
            try:
                if count_words.count(word) > 1:
                    layout.lbl_poem['text'] = f"Error:\nDo not enter duplicated words please."
                    return
                elif word == "" or word == " ":
                    layout.lbl_poem['text'] = f"Error:\nDo not enter blank spaces " \
                                              f"or commas at the end please."
                    return
                word_regex.search(word).group()

            except (NameError, AttributeError):
                layout.lbl_poem['text'] = f"Error:\nOnly enter letters please."
                return
        if "" not in words:
            clean_entries.append(words)

    noun, verbs, adj, prep, adv = clean_entries

    if len(noun) == 3 and len(verbs) == 3 \
            and len(adj) == 3 and len(prep) == 2 and len(adv) == 1:

        # Random nouns
        noun1, noun2, noun3 = random.choice(noun), random.choice(noun), random.choice(noun)
        while noun1 == noun2 or noun1 == noun3 or noun2 == noun3:
            noun1, noun2, noun3 = random.choice(noun), random.choice(noun), random.choice(noun)

        # Random verbs.
        verb1, verb2, verb3 = random.choice(verbs), random.choice(verbs), random.choice(verbs)
        while verb1 == verb2 or verb1 == verb3 or verb2 == verb3:
            verb1, verb2, verb3 = random.choice(verbs), random.choice(verbs), random.choice(verbs)

        # Random adjectives
        adj1, adj2, adj3 = random.choice(adj), random.choice(adj), random.choice(adj)
        while adj1 == adj2 or adj1 == adj3 or adj2 == adj3:
            adj1, adj2, adj3 = random.choice(adj), random.choice(adj), random.choice(adj)

        # Random prepositions
        prep1, prep2, = random.choice(prep), random.choice(prep)
        while prep1 == prep2:
            prep1, prep2= random.choice(prep), random.choice(prep)

        layout.lbl_poem['text'] = f"{a_or_an(adj1, start=1)} {noun1}.\n\n" \
                                  f"{a_or_an(adj1, start=1)} {noun1} {verb1} " \
                                  f"{prep1} {adj2} {noun2}\n{adv[0]}, the {noun1} " \
                                  f"{verb2}\nthe {noun2} {verb3} {prep2} " \
                                  f"{a_or_an(adj3)} {noun3}.\n"
    else:
        layout.lbl_poem['text'] = error_msj
