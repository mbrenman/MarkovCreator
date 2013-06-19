#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matt Brenman
#
# Created:     04/06/2013
# Copyright:   (c) Matt Brenman 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def main():
    words = "On and on and on.".split()
    triples = get_triples(words)
    starters = get_starters(words)

    first_word, second_word = get_two_words(starters)
    next_word = ''
    print first_word + " " + second_word,
    for i in range(25):
        if (first_word, second_word) not in triples:
            first_word, second_word = get_two_words(starters)
            print first_word + " " + second_word,

        rand_index = random.randrange(0, len(triples[(first_word, second_word)]))
        next_word = triples[(first_word, second_word)][rand_index]

        print next_word,
        first_word, second_word = second_word, next_word


def get_triples(words):
    triples = {}
    for i in range(len(words) - 2):
        if (words[i], words[i+1]) in triples:
            triples[(words[i], words[i+1])].append(words[i+2])
        else:
            triples[(words[i], words[i+1])] = [words[i+2]]
    return triples

def get_starters(words):
    starters = {}
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i+1]
        if (word[0].isupper()):
            starters[word] = next_word
    return starters

def get_two_words(starters):
    first_list = starters.keys()
    index = random.randrange(0, len(first_list))
    first_word = first_list[index]
    return first_word, starters[first_word]

if __name__ == '__main__':
    main()
