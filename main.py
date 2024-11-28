def main():
  book_path = 'books/frankenstein.txt'
  book_text = get_book_text(book_path)
  word_count = count_book(book_text)
  character_count = count_characters(book_text)
  new_clean_list = clean_list(character_count)
  print_report(book_path, word_count, new_clean_list)

  

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def count_book(book):
  split_book = book.split()
  return len(split_book)

def count_characters(book):
  character_store = {}
  for char in book:
    lowered = char.lower()
    if lowered in character_store:
      character_store[lowered] += 1
    else:
      character_store[lowered] = 1
  return character_store
    
# print report function, takes in book path, word count, character count
def clean_list(character_count_dict):
  # convert character count to list of dictionaries
  list_of_chars = convert_dict_to_list(character_count_dict)
  # sort list
  list_of_chars.sort(reverse=True, key=sort_on)
  return list_of_chars

# function to convert dictionary to list, accepts cc dictionary
def convert_dict_to_list (dict):
  new_list = []
  for item in dict:
    if item.isalpha():
      new_list.append({"name": item, "num": dict[item]})
  return new_list
# function to sort list of dictionaries
def sort_on(dict):
  return dict["num"]
# function to return 
def print_report(book_path, word_count, list):
  print(f"---Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print()
  for char_dict in list:
    print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")
  print("--- End report ---")

main()