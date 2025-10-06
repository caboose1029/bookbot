import sys
from stats import count_words, count_chars, generate_report

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        contents = f.read()
        return contents

def main() -> None:
    # text = get_book_text("./books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    num_chars = count_chars(text)
    report = generate_report(num_chars)
    print_report("books/frankenstein.txt", num_words, report)

def print_report(filepath, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_count:
        if character["char"].isalpha():
            print(character["char"] + ": " + str(character["num"]))
    print("============= END ===============")




if __name__ == "__main__":
    main()
