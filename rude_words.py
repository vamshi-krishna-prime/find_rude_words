import os
rude_words_list = ["idiot",
                   "lazy",
                   "crazy",
                   "damn",
                   "fool",
                   "stupid",
                   "jerk",
                   "darn"]

def check_line(line, count):
    rude_words_line_count = 0
    words = line.split(" ")
    for word in words:
        if word in rude_words_list:
            rude_words_line_count += 1
            print(f"Rude word found: {count + 1}. {word}\n")
    return rude_words_line_count


def check_file(filename):
    with open(filename) as my_file:
        rude_words_count = 0
        for line in my_file:
            rude_words_count += check_line(line, rude_words_count)
    print(f"Total Rude Words Found: {rude_words_count}")
    if rude_words_count == 0:
        print("Congratulations there are no rude words found")
        print("Atleast none I know of")


if __name__ == "__main__":
    check_file("rude_passage.py")
