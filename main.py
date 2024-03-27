def main():
    with open('books/frankenstein.txt') as f:
        # the file is f
        file_contents = f.read()
        # the content of the file is saved as a variable
        # print(file_contents)

        words = file_contents.split()
        # takes the book and makes a list of all words
        words_total = len(words)
        # counts how long the list is (how many words)
        # print(f"The book contains {words_total} words.\n")

        char_count = {}
        # empty dictionary to fill
        lowered_book = file_contents.lower()
        # lower case the book
        for letter in lowered_book:
            # loops through every letter in the string
            if letter.isalpha():
                # if the character is alphabetical proceed
                if letter in char_count:
                    char_count[letter] += 1
                # if the character is in the dictionary. add 1
                else:
                    char_count[letter] = 1
                # otherwise add the character and set it to 1
        # print(char_count)



        char_list = []
        # empty list for dictionaries.
        for char, count in char_count.items():
            # iterates through each item in the char_count dict
            char_dict = {"char": char, "num":count}
            # creates a new dictionary for each character
            char_list.append(char_dict)
            # add the dictionary to the list
        char_list.sort(reverse=True, key=sort_on)
        # sorts the list in descending order (reverse=True) and using 

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_total} words found in the document")
        
        for item in char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")


def sort_on(dict):
    return dict["num"]

if __name__ == "__main__":
    main()