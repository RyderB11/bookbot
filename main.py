def main():
    with open('books/Frankenstein.txt') as f:
        frankenstein = f.read()
        count_dict = counting(frankenstein)
        new_list = transform_and_sort(count_dict)

        print("--- Begin report of books/Frakenstein.txt ---")
        print(f"{word_count(frankenstein)} words found in the documnet")

        for entry in new_list:
            print(f"The {entry['character']} character was found {entry['count']} times")

                  
        print("---- End of report ----")

# counting function takes the text given to count the letters of the text. first it is case sensitive, so we make them all the same with text.lower(). next we create a dictionary.
# we start the loop for the letters in the loop. the if statement checks if the char is a letter. if it is then it does the function .
# first we define the dict to update it by simply counter[char] = , then counter.get is checking the dict. we do (char,0) +1. the char is checking if the key is in the dict
# if it is then +1, if it is not, it returns 0, we put the 0 specifically becuase without it, it returns "none" and will not work.
def counting(text):
    lowered_string = text.lower()
    counter = {}
    for char in lowered_string:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    return counter

# word_count is a function that takes whatever text parameter and counts the words. we call it in the main() and feed it the Frankenstein as a parameter.
def word_count(text):
    words = text.split()
    return(len(words))


def sort_on(dictionary):
    return dictionary["count"]



def transform_and_sort(count_dict):
    list_of_dicts = []
    for key, value in count_dict.items():
        list_of_dicts.append({"character": key, "count": value})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts



main()