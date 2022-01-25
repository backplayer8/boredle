# -*- coding: utf-8 -*-

from os import system as do
from typing import List, Set, Union

from english_words import english_words_lower_alpha_set as wordlist


def cls():
    """
    cls clears the terminal. Used when accidentally calling wordlist
        containing 25,xxx words.
    """
    do("clear")


def prep_wordlist(wordlist, size: int = 5):
    """
    prep_wordlist creates a new list of strings with a len(5) by default,
        returns a list of strings.

    Arguments:
        wordlist {list[str]} -- a list of words as strings.

    Returns:
        list -- a list of strings that match the length specified.
    """
    return [word for word in wordlist if len(word) == 5]


def exclude_by_char(chars, words):
    """
    exclude_by_char iterates a list of words, picking out only words without
        characters matching <chars>, returning a new list of words.
        * Use this with characters that have black squares.

    Arguments:
        chars {str} -- string of characters to exclude words from the new list.
        words {list[str]} -- The wordlist to pick from.

    Returns:
        [list] -- A new list of words that do not contain the characters specified.
    """
    return [word for word in words if all(char not in word for char in chars)]


def include_by_char(chars, wordlist):
    """
    include_by_char iterates a list of wordsm picking out only words that contain
        charcters matching <chars>, returning a new list of words.
        * Use this with characters that have a yellow box after guessing ie. the
        character belongs in the word but the location is unknown.

    Arguments:
        chars {str} -- a string of characters that belong in the word.
        wordlist {list} -- a list of words that contain the characters.

    Returns:
        [type] -- [description]
    """
    return [word for word in wordlist if all(char in word for char in chars)]


def lock_in_index(characters, indices, words):
    """
    lock_in_index selects all words from a list that contain specific characters
        at specific index in the word, creating a new set of words.

    Arguments:
        characters {str} -- a string of letters in any order, so long as the order
            is maintained in <indices>
        indices {list|str} -- numerical index where each character should occur,
            must follow order of <characters>.
        words {list} -- a list of words to select from.

    Raises:
        ValueError: <characters> and <indices> must be of the same length.

    Returns:
        set -- a new set of words matching the criteria specified in
        <characters> and <indices>.
    """

    if len(characters) != len(indices):

        raise IndexError("Number of characters should equal number of indexes")
    return [
        word
        for word in words
        if all(word[idx] == char for char, idx in zip(characters, indices))
    ]


def lock_out_index(char, indices, words):
    """
    lock_out_index iterates a list of words and picks only words that have no matching
    characters at the specified index. Used to narrow down the selection by ensuring a
    yellow box on the guess does not contain the letter that we know does not belong
    there.

    Arguments:
        char {[type]} -- [description]
        indices {[type]} -- [description]
        words {[type]} -- [description]

    Raises:
        IndexError: [description]

    Returns:
        [type] -- [description]
    """
    if len(char) != len(indices):
        raise IndexError("Number of characters should equal number of indexes")

    return [
        word for word in words if all(word[idx] != ch for ch, idx in zip(char, indices))
    ]


words = prep_wordlist(wordlist)


def v1_lock_in_index(characters: str, indices: List[Union[int, str]], words) -> set:
    """
    v1_lock_in_index selects all words from a list that contain specific characters
        at specific index in the word, creating a new set of words.

    Arguments:
        characters {str} -- a string of letters in any order, so long as the order
            is maintained in <indices>
        indices {list|str} -- numerical index where each character should occur,
            must follow order of <characters>.
        words {list} -- a list of words to select from.

    Raises:
        ValueError: <characters> and <indices> must be of the same length.

    Returns:
        set -- a new set of words matching the criteria specified in
        <characters> and <indices>.
    """
    if len(characters) != len(indices):
        raise ValueError("Number of characters should equal number of indexes")

    if isinstance(indices, str):
        indices = [int(num) for num in indices.replace(" ", "")]

    for char, idx in zip(characters, indices):
        words = set([word for word in words if word[idx] == char])

    return words
