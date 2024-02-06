# 1. create a list of random number of dicts (from 2 to 10)

import random
import string

letters = ['a', 'b', 'c', 'd']

def list_of_rand_dicts(nr_of_dicts):
    random_dicts = [{letter: random.randint(0,100) for letter in letters} for _ in range(nr_of_dicts)]
    return random_dicts


# 2. get previously generated list of dicts and create one common dict:

def common_dict(list_of_dicts):
    common_dict = {}
    for letter in letters:
        max_value = max(d[letter] for d in list_of_dicts if letter in d)
        common_dict[letter] = max_value
    return common_dict


# 3 - text task

import re

text_variable = "homEwork:\n\n tHis iz your homeWork, copy these Text to variable.\n\n You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n\n it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

def create_sentences(text):
    return text.split('.')

def add_sentence_lwords(text, sentences):
    last_words = [sentence.split()[-1] for sentence in sentences if sentence]
    return text + ' ' + ' '.join(last_words)
    
def resolve_mistakes(text):
    return re.sub(r"\biz\b",'is',text).capitalize()

def count_whitespaces(new_text):
    count_of_whitespaces = 0
    for i in new_text:
        if i.isspace():
            count_of_whitespaces += 1
    return count_of_whitespaces


new_text = resolve_mistakes(add_sentence_lwords(text_variable, create_sentences(text_variable)))

print(new_text, f"\nthere are {count_whitespaces(new_text)} whitespaces.")


