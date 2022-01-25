from english_words import english_words_lower_alpha_set as wordlist
from secrets import choice


class Boredle(object):
    def __init__(self):
        self._wordlist = [word for word in wordlist if len(word) == 5]
        self.first_guess = None
        self.second_guess = None
        self.third_guess = None
        self.fourth_guess = None
        self.fifth_guess = None
        self.sixth_guess = None
        self.first_guess = self.guess()
        self._correct = {}
        print(f"Suggested first guess is: {self.first_guess}")

    def __repr__(self) -> str:
        return f"""{__class__.__name__}(First_Guess: {self.first_guess}, Second_Guess: {self.second_guess}, Third_Guess: {self.third_guess}, Fourth_Guess: {self.fourth_guess}, Fifth_Guess: {self. fifth_guess}, sixth_guess: {self.sixth_guess}"""

    def guess(self):
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

    @property
    def words(self):
        return self._wordlist

    def prep_wordlist(self, size: int = 5):
        return [word for word in self._wordlist if len(word) == size]

    def exclude_by_char(self, chars):
        self._wordlist = [
            word for word in self._wordlist if all(char not in word for char in chars)
        ]

    def include_by_char(self, chars):
        self._wordlist = [
            word for word in self._wordlist if all(char in word for char in chars)
        ]

    @property
    def correct_characters(self):
        return self._correct

    @correct_characters.setter
    def correct_characters(self, chars_idxs):
        try:
            chars, indexes = chars_idxs
        except ValueError as err:
            raise(ValueError(err, 'Accepts a tuple like: ("chars", [0, 1, 2, 3, 4])'))
        else:
            if len(chars) != len(indexes):
                raise(ValueError("string length must be the same as number of indexes"))

            self._correct.update({index:char for char, index in zip(chars, indexes)})
        

    def lock_in_index(self, characters, indices):

        if len(characters) != len(indices):

            raise IndexError("Number of characters should equal number of indexes")
        self._wordlist = [
            word
            for word in self._wordlist
            if all(word[idx] == char for char, idx in zip(characters, indices))
        ]

    def lock_out_index(self, char, indices):
        if len(char) != len(indices):
            raise IndexError("Number of characters should equal number of indexes")

        self._wordlist = [
            word
            for word in self._wordlist
            if all(word[idx] != ch for ch, idx in zip(char, indices))
        ]
