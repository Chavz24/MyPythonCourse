"""Challenge: Return of the Poet 18.10"""

import re

# The generate button function.

word_regex = re.compile("^[A-Za-z]*$")


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


def generate_button():
    """This function checks the entries widgets and generate a poem.
        It also checks if the words are repeated ot if there aren't enough words."""

    import O_Visual_layout_Challenge as layout

    raw_entries = [
        layout.ent_word_noun, layout.ent_word_verb, layout.ent_word_adj,
        layout.ent_word_prep, layout.ent_word_adv
    ]
    clean_entries = []
    error_msj = f"Error:\nYou have to enter " \
                f"\n3 nous, 3 verbs,3 adjectives" \
                f"\n3 prepositions and on adverb."

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

    correct_entries = 0
    for word_list in clean_entries:

        if len(word_list) == 3:
            correct_entries += 1
        else:
            layout.lbl_poem['text'] = error_msj

    if correct_entries == 4:
        noun, verbs, adj, prep, adv = clean_entries
        # {A/An} {adj1} {noun1}
        # {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
        # {adverb1}, the {noun1} {verb2}
        # the {noun2} {verb3} {prep2} a {adj3} {noun3}
        if len(noun) == 3 and len(verbs) == 3 \
                and len(adj) == 3 and len(prep) == 3 and len(adv) == 1:
            layout.lbl_poem['text'] = f"{a_or_an(adj[0],start=1)} {noun[0]}.\n\n" \
                                      f"{a_or_an(adj[0],start=1)} {noun[0]} {verbs[0]} " \
                                      f"{prep[0]} the {adj[1]} {noun[1]}\n{adv[0]}, {noun[0]} " \
                                      f"{verbs[1]}\n the {noun[1]} {verbs[2]} {prep[1]} " \
                                      f"{a_or_an(adj[2])} {noun[2]}.\n"
        else:
            layout.lbl_poem['text'] = error_msj
    else:
        layout.lbl_poem['text'] = error_msj


# todo add choice