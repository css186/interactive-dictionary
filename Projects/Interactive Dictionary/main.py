# import packages nedded
import json
import sys
import difflib
import os

# difflib introduction:
"""
difflib.SequenceMatcher 判斷兩個字串的相關性 
第一個參數預設為None, 使用ration()方法後會返回一個相關係數的值
ratio = difflib.SequenceMatcher(None, "accident", "accccident").ratio()


difflib.get_close_matches方法
收兩個參數，第一個為目標字串，第二個為字串list
結果回返回與目標字串相近的字串list(相關係數>0.6)
close_item = difflib.get_close_matches("accident", ["apple", "banana", "car", "accddddent", "accidentally"])
print(close_item) -> ['accidentally', 'accddddent']
"""

# 0. find the filepaht of data.json file by using os
dir_path = os.path.abspath(os.path.join("."))
data_path = dir_path + "/Resources/data.json"

# 1. read data.json to variable
dictionary_data = json.load(open(data_path))
# test data reading
# print(dictionary_data["abandoned vehicle"])
# print(dictionary_data)

# 2. define functions:
def search_dict(dict, str):
    """
    :param dict: take dictionary_data as a dict
    :param str: take user's input string as value to lookup keys in the dict
    :return: an fstring (output)
    """
    meanings = dict[str]
    print()
    output = "\n"
    output = f"The Word '{str}' means: \n"
    for index, meaning in enumerate(meanings, start = 1):
        output += f"{index}. {meaning}\n"
    return output

# test function
# print(search_dict(dictionary_data, "abandoned vehicle"))

# 3. initializing interaction with users
# text coloring
sys.stdout.write("\033[1;36m")
flag = False

while (flag == False):

    search = input("Please Enter a Word You Want to Search: ")

    # initializing
    search = search.lower()
    # store keys of dict into a list
    dictionary_data_keys = list(dictionary_data.keys())
    output = None
    identical_words = difflib.get_close_matches(search, dictionary_data_keys)
    identical_words_len = len(identical_words)

    # error handling
    # set not case sensitive
    if search in dictionary_data:
        output = search_dict(dictionary_data, search)
        print(output)
        flag = True
        break
    # return identical word list if word length larger than zero
    elif identical_words_len > 0:
        for identical in identical_words:
            if identical_words_len == 1:
                next_input = input(f"Do you mean '{identical}' ? (Enter Y to Continue / N to Retry): ")
            else:
                next_input = input(f"Do you mean '{identical}' ? There are {identical_words_len - identical_words.index(identical) - 1} more choices. (Enter Y to Continue / N to Retry):")

            if next_input.lower() == "y":
                output = search_dict(dictionary_data, identical)
                print(output)
                flag = True
                break
            elif next_input.lower() == "n":
                pass
            else:
                output = "Invalid Input. Please Try Again!"
                print(output)
                break
    else:
        output = f"Sorry. We Cannot Find '{search}'"
        print(output)
        pass
