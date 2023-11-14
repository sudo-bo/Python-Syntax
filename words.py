def print_upper_words(words):
    """ Print a list of words entirely in uppercase (only if they begin with the letter e :))"""
    for word in words:
        if word[0].lower() == "e":
            print(f"{word.upper()}")

def print_upper_words2(words, letter):
    """ Print a list of words entirely in uppercase (only if they begin with the letter e :))"""
    for word in words:
        if word[0].lower() == letter.lower():
            print(f"{word.upper()}")


print(print_upper_words(["Each", "easter", "love", "shelly beamer"]))


print(print_upper_words2(["Each", "easter", "love", "shelly beamer"], "s"))
