import os
rude_words_list = ["idiot",
                   "lazy",
                   "crazy",
                   "damn",
                   "fool",
                   "stupid",
                   "jerk",
                   "darn"]

with open("rude_passage.py") as my_file:
    contents = my_file.read()
    words = contents.split(" ")
    rude_words_count = 0
    for word in words:
        if word in rude_words_list:
            rude_words_count += 1
            print(f"Rude word found: {rude_words_count}. {word}\n")

if rude_words_count == 0:
    print("Congratulations there are no rude words found")
    print("Atleast none I know of")
