# Refer to this module's readme
from helpers import get_words, save_counts

def main():
    words = get_words("c:\\Users\\rself\\OneDrive\\Documents\\GitHub\\CSC121\\CSC121\\src\\module_2\\address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    save_counts(counts)

main()