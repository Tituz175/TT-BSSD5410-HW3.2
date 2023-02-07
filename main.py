import string
import re


def process_file(fname, enc):
    with open(fname, "r", encoding=enc) as file:
        dat = file.read()
        dat = perform_re(dat)
    return dat.split()


# end def process_file(fname, enc):

def write_results(fname, data, enc):
    with open(fname, "w", encoding=enc) as file:
        file.write(data)


# end def write_results(fname, data, enc):


def words_to_dict(all_words, dictionary):
    for word in all_words:
        word = clean_word(word)
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1


# end def words_to_dict(all_words, dictionary):


def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")
    return word.lower()


# end def clean_word(word):


def perform_re(text):
    text = re.sub(r"(CHAPTER) ([IVXLC]+.)", "\\1\\2", text)
    return text


# end def perform_re(text):

def book_statistics(selected_books):
    book_one_word_len = 0
    book_two_word_len = 0
    general_unique_words = []
    words_difference = 0
    for num in range(len(selected_books)):
        words = process_file(f"{selected_books[num]}.txt", "utf-8")
        unique_words = {}
        general_unique_words.append(unique_words)
        words_to_dict(words, unique_words)
        print(f"====================================================")
        print(f"\t\t\t{selected_books[num].upper()}")
        print(f"The book has {len(unique_words.keys())} unique words.")
        if num == 0:
            book_one_word_len = len(words)
        else:
            book_two_word_len = len(words)
        print(f"The total word count of the book is {len(words)}.")
        print(f"The book's Type Token Ratio is {len(unique_words.keys()) / len(words)}.")
        print(f"====================================================\n")
        words_difference = abs(book_one_word_len - book_two_word_len)
    if words_difference > 3000:
        print("\nType Token Ratio is not a reliable comparison for chosen texts")
    else:
        print("\nType Token Ratio is between comparable texts")
    return general_unique_words


# end def book_statistics(selected_books):

def word_search(general_unique_words, selected_books, choice, result):
    word_dic = {}
    for num in range(len(general_unique_words)):
        if choice in general_unique_words[num].keys():
            if num in word_dic:
                word_dic[num] += general_unique_words[num].get(choice, 0)
            else:
                word_dic[num] = general_unique_words[num].get(choice, 0)
            result += general_unique_words[num].get(choice, 0)
        else:
            result += general_unique_words[num].get(choice, 0)
    if result:
        print(
            f"\nThe word '{choice}' appears in {selected_books[0]}.txt {word_dic[0]} times and {selected_books[1]}.txt {word_dic[1]} times and with a total of {result} times in both texts.")
    else:
        print(f"\nThe word '{choice}' appears 0 times in both texts")


# end def word_search(general_unique_words, selected_books, choice, result):


def main():
    list_of_books = ["alice", "anne", "peter pan", "secret garden", "wonderful wizard"]
    selected_books = []
    print("================Welcome================")
    print("\tKey\tBook title")
    for i in range(len(list_of_books)):
        print(f"\t{i + 1}\t{list_of_books[i].capitalize()}")
    choice = input("\nEnter two book keys you wish to compare separated by comma: ")
    book_one = int(choice.split(",")[0]) - 1
    book_two = int(choice.split(",")[1]) - 1
    selected_books.append(list_of_books[book_one])
    selected_books.append(list_of_books[book_two])
    general_unique_words = book_statistics(selected_books)
    choice = input("\nKindly select another book for comparison: ")
    selected_books[1] = list_of_books[int(choice) - 1]
    general_unique_words = book_statistics(selected_books)
    choice = input("\nKindly supply the word you will like to search through the texts: ")
    result = 0
    word_search(general_unique_words, selected_books, choice, result)


# end def main():

if __name__ == '__main__':
    main()
