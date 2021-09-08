"""Challenge: Return of the Poet 18.10"""


# The generate button function.


def generate_button():
    """This function checks the entries widgets and generate a poem.
        It also checks if the words are repeated ot if there aren't enough words."""
    import O_Visual_layout_Challenge as layout

    labels = [
        layout.lbl_word_noun, layout.lbl_word_verb, layout.lbl_word_adj,
        layout.lbl_word_prep, layout.lbl_word_adv
    ]
    entries = [
        layout.ent_word_noun, layout.ent_word_verb, layout.ent_word_adj,
        layout.ent_word_prep, layout.ent_word_adv
    ]
    number_check = [3, 3, 3, 3, 1]
    for entry_box in entries:
        count_words = entry_box.get().split(",")

        if len(entry_box.get().split(",")) == number_check[entries.index(entry_box)] \
                and "" not in count_words:
            if len(count_words) <= len(set(count_words)):
                layout.lbl_poem['text'] = f"Error:\nDo not enter duplicated words please."
                return # todo
            layout.lbl_poem['text'] = f"it works{number_check[entries.index(entry_box)]}"
        else:

            layout.lbl_poem['text'] = f"Error:\nYou have to enter " \
                                      f"\n3 nous, 3 verbs,3 adjectives" \
                                      f"\n3 prepositions and on adverb."

            return



