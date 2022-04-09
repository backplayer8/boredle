#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
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


@pytest.mark.parametrize("chars, wordlist", [("hae", ["hear", "stear", "earth"])])
def test_include_by_char(chars, wordlist):
    words = include_by_char(chars, wordlist)
    assert len(words) == 2
    assert "hear" in words and "earth" in words


@pytest.mark.parametrize(
    "chars, wordlist", [("pn", ["pander", "elate", "loose", "ponsi", "store"])]
)
def test_exclude_by_char(chars, wordlist):
    words = exclude_by_char(chars, wordlist)
    assert len(words) == 3
    assert "elate" in words
    assert "loose" in words
    assert "store" in words
