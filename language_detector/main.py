# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from collections import Counter

def detect_language(text, languages):
    """Returns the detected language of given text."""
    lang_most = None
    lang_count = 0
    for language in languages:
        count = len([x for x in language["common_words"] if x in text])
        if count > lang_count:
            lang_count = count
            lang_most = language["name"]
    return lang_most

def most_common_word(text, frequency=1):
    count = 0
    most_word = []
    common_words = Counter(text.rsplit())
    for key,val in common_words.items():
        if val > frequency:
            most_word.append([key,val])
    most_word.sort(key=lambda x: x[1], reverse=True)
    return most_word

def percent_word_used(common_word, text):
    freq = []
    for word, occur in common_word:
        freq.append([word, (100 * occur / len(text.rsplit()))])
    return freq

def stats(common_word, percent):
    return ("The most common word,'{}', occured {} times " 
            "and comprises approximately {}% of the " 
            "text.").format(common_word[0][0],common_word[0][1],percent[0][1])
