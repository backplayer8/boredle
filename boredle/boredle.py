from copy import copy
from tkinter import N
from english_words import english_words_lower_alpha_set as wordlist
from secrets import choice
from typing import Union


class Boredle(object):
  
    def __init__(
        self,
        first_guess: Union[str, None]=None,
        second_guess: Union[str, None]=None,
        third_guess: Union[str, None]=None,
        fourth_guess: Union[str, None]=None,
        fifth_guess: Union[str, None]=None,
        sixth_guess: Union[str, None]=None,
    ):
        self._wordlist = [word for word in wordlist if len(word) == 5]
        self.first_guess = self.guess() if first_guess is None else first_guess
        self.second_guess = second_guess
        self.third_guess = third_guess
        self.fourth_guess = fourth_guess
        self.fifth_guess = fifth_guess
        self.sixth_guess = sixth_guess
        self._correct_letters = {
            0: None,
            1: None,
            2: None, 
            3: None,
            4: None,
        }
        print(f"Suggested first guess is: {self.first_guess}")

    def __repr__(self) -> str:
        return f"""{__class__.__name__}(
            first_guess="{self.first_guess}",
            second_guess="{self.second_guess}",
            third_guess="{self.third_guess}",
            fourth_guess="{self.fourth_guess}",
            fifth_guess="{self. fifth_guess}",
            sixth_guess="{self.sixth_guess}"
            )"""

    def guess(self, _guess:Union[str, None]=None) -> str:
        match None:
            case self.first_guess:
                self.first_guess = choice(self._wordlist)
                return self.first_guess
            case self.second_guess:
                self.second_guess = choice(self._wordlist)
                return self.second_guess
            case self.third_guess:
                self.third_guess = choice(self._wordlist)
                return self.third_guess
            case self.fourth_guess:
                self.fourth_guess = choice(self._wordlist)
                return self.fourth_guess
            case self.fifth_guess:
                self.fifth_guess = choice(self._wordlist)
                return self. fifth_guess
            case self.sixth_guess:
                print("Final Guess!")
                self.sixth_guess = choice(self._wordlist)
                return self.sixth_guess
            case _:
                print("Game Over!")

    def educated_guess(self, *chars):
        words = copy(self._wordlist)
        common_words = []
        for char in chars:
            common_words.extend([word for word in words if char in word])
        return common_words

    def _guess(self):
        words = copy(self._wordlist)
        word = choice(words)
        if all([False for char in word if word.count(char) != 1]):
            words.remove(word)
            return word
        else:
            return self.guess()

    def redo_guess(self, _guess):
        if _guess is not None:
            pass

    def redo_guess(self, criteria=None, guess=None):
        match type(str):
            case self.sixth_guess:
                self.sixth_guess = None
            case self.fifth_guess:
                self.fifth_guess = None
            case self.fourth_guess:
                self.fourth_guess = None
            case self.third_guess:
                self.third_guess = None
            case self.second_guess:
                self.second_guess = None
            case self.first_guess:
                self.first_guess = None
            case _:
                raise ValueError("criteria must be None or valid state for a string")
        

    @property
    def words(self):
        return self._wordlist

    def _prep_wordlist(self, size: int = 5):
        return [word for word in self._wordlist if len(word) == size]

    def exclude_by_char(self, chars:Union[str,list[str]]) -> None:
        """exclude_by_char is to be called when you have characters not in
        the word at all. e.g. the letter inside a black box. Removes words
        with the incorrect letters.

        Args:
            chars (str): The characters to exclude. Should not contain any
            characters except a-z.
        """
        self._wordlist = [
            word for word in self._wordlist if all(char not in word for char in chars)
        ]

    def include_by_char(self, chars:Union[str,list[str]]) -> None:
        """include_by_char is to be called when you have characters in
        the word either in the correct or incorrect index is fine. e.g.
        the letter inside a black box. Removes words from the list that
        do not contain the letters passed to the function.

        Args:
            chars (_type_): _description_
        """
        self._wordlist = [
            word for word in self._wordlist if all(char in word for char in chars)
        ]

    @property
    def correct_letters(self):
        return self._correct_letters

    @correct_letters.setter
    def correct_characters(self, chars_idxs):
        try:
            chars, indexes = chars_idxs
        except ValueError as err:
            raise (ValueError(err, 'Accepts a tuple like: ("chars", [0, 1, 2, 3, 4])'))
        else:
            if len(chars) != len(indexes):
                raise (
                    ValueError("string length must be the same as number of indexes")
                )

            self._correct_letters.update({index: char for char, index in zip(chars, indexes)})

    def count_remaining_words(self):
        return len(self._wordlist)

    def lock_in_index(self, characters: str, indices: Union[str, list[int]]):
        if len(characters) != len(indices):
            raise IndexError("Number of characters should equal number of indexes")

        if isinstance(indices, str):
            indices = [int(num) for num in indices]

        self._wordlist = [
            word
            for word in self._wordlist
            if all(word[idx] == char for char, idx in zip(characters, indices))
        ]
        self.correct_characters = (characters, indices)

    def lock_out_index(self, char: str, indices: Union[str, list[int]]):
        if len(char) != len(indices):
            raise IndexError("Number of characters should equal number of indexes")

        if isinstance(indices, str):
            indices = [int(num) for num in indices]

        self._wordlist = [
            word
            for word in self._wordlist
            if all(word[idx] != ch for ch, idx in zip(char, indices))
        ]

    def filter_multiples(self, char: str, repeats: int):
        self._wordlist = [
            word for word in self._wordlist if word.count(char) == repeats
        ]
        
