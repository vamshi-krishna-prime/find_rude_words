import os
rude_words_list = ["idiot",
                   "lazy",
                   "crazy",
                   "damn",
                   "fool",
                   "stupid",
                   "jerk",
                   "darn"]

with open("greeting.py") as my_file:
    contents = my_file.read()
    rude_words_count = 0

    for rude_word in rude_words_list:
        if rude_word in contents:
            rude_words_count += 1
            print(f"Rude word found: {rude_words_count} {rude_word}\n")

if rude_words_list == 0:
    print("Congratulations there are no rude words found")
    print("Atleast none I know of")
