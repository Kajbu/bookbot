def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    lowercase_text = make_lowercase(text)
    character_dictionary = count_characters(lowercase_text)
    character_dictionary.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for i in character_dictionary:
        current_char = get_char(i)
        current_num = sort_on(i)
        print(f"The '{current_char}' character was found {current_num}times")
        

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def make_lowercase(text):
    lowered_string = text.lower()
    return lowered_string

def sort_on(dict):
    return dict["num"]

def get_char(dict):
    return dict["char"]

def count_characters(text):
    list = []
    for i in text:
        if i.isalpha():
            exists = False
            for d in list:
                if d["char"] == i:
                    exists = True
                    d["num"] += 1
                    break
            if not exists:
                list.append({"char": i, "num": 1})
    return list


                


        #if i in dictionary:
        #    dictionary[i] = dictionary[i] + 1
        #else:
        #    dictionary[i] = 1




    


main()