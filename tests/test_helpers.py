#!/usr/bin/env python
# -*- coding: utf-8 -*-
from english_words import english_words_lower_alpha_set as wordlist
from wordle.helpers import (
    exclude_by_char,
    include_by_char,
    lock_in_index,
    lock_out_index,
    prep_wordlist,
)


def test_wordlist():
    words = prep_wordlist(wordlist)
    assert all([len(word) == 5 for word in words])
