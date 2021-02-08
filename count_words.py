#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def read_file(file_path):
    test_file = open(file_path, "r")
    test_words = test_file.read()
    test_file.close()
    return test_words

def save_result(result, file_path):
    output_file = open(file_path, "w")
    output_file.write(result)
    print("Save completed")

def count_word(input_str):
    count_words = input_str.split()
    count_dict = {}
    for word in count_words:
        word = word.lower()
        if word not in count_dict.keys():
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return count_dict

def get_max(count_dict):
    max_count = max(count_dict.values())
    max_words = []
    for word, count in count_dict.items():
        if count == max_count:
            max_words.append(word)
    return max_words, max_count

def get_localtime():
    localtime = time.localtime()
    return time.strftime("%H:%M:%S", localtime) 

def convert2str(*args):
    output_str = "The words and corresponding times:\n"
    for arg in args:
        try:
            if type(arg) == list:
                tmp_str = " ".join(arg)
                output_str += tmp_str
            elif type(arg) == int or type(arg) == str:
                output_str += " : "
                output_str += str(arg)
        except:
            print("Error, unknown type:", type(arg))
    return output_str

if __name__ == '__main__':
    test_words = read_file("test_words.txt")
    count_result = count_word(test_words)
    max_words, max_count = get_max(count_result)
    print("check_time:", get_localtime())
    print("check_result:", max_words, max_count)
    output_str = convert2str(max_words, max_count)
    save_result(output_str, "test_word_result.txt")
