#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []

    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


def make_exclamation(sentence_list):
    modified_sentences = []

    if not sentence_list:
        return modified_sentences

    for sentence in sentence_list:
        modified_sentence = sentence + "!"  
        modified_sentences.append(modified_sentence)  

    return modified_sentences