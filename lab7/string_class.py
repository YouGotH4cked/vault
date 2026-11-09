import random
import string
"""
Implement a class MyString that behaves like a Python string but only allows lowercase
characters, and, in contrast to Python's str, allows modifications like changing a character within a
string in place (i.e. MyString is mutable).
"""

class MyString:

    def __init__(self, sequence=None, initialize_with_random=False):
        if initialize_with_random:
            n = random.randint(1, 10)

            self._chars = [
                random.choice(string.ascii_lowercase) for _ in range(n)
            ]

        elif sequence is not None:
            if not isinstance(sequence, str):
                raise TypeError("Input must be a string.")

            if not all(char in string.ascii_lowercase for char in sequence):
                raise ValueError(
                    "String must contain only lowercase characters."
                )

            self._chars = list(sequence)

        else:
            self._chars = []


    def __str__(self):
        return "".join(self._chars)
        #result = "".join(self._chars) + "\n"
        #for index, char in enumerate(self._chars):
        #   result += f"Character at position {index}: {char}\n"
        #return result.strip()


    def __getitem__(self, key):
        if isinstance(key, slice):
            return MyString("".join(self._chars[key]))
        return self._chars[key]


    def __setitem__(self, index, value):
        if (
            not isinstance(value, str)
        ):
            raise TypeError("Must be a string.")
        elif (
            len(value) != 1
        ):
            raise TypeError("Must be a single character.")
        elif (
            value not in string.ascii_lowercase and value not in string.ascii_uppercase
        ):
            raise TypeError("Cannot add non-letter character")
        elif (
            value not in string.ascii_lowercase
        ):
            raise TypeError("Cannot add uppercase character")

        self._chars[index] = value


    def replace(self, old, new, count=-1):
        old_str = str(old) if isinstance(old, MyString) else old
        new_str = str(new) if isinstance(new, MyString) else new

        if not isinstance(old_str, str) or not isinstance(new_str, str):
            raise TypeError("Substrings must be strings.")

        if not all(char in string.ascii_lowercase for char in new_str):
            raise TypeError(
                "Replacement string must contain only lowercase characters."
            )

        current_text = "".join(self._chars)

        if count == -1:
            replaced_text = current_text.replace(old_str, new_str)
        else:
            replaced_text = current_text.replace(old_str, new_str, count)

        self._chars = list(replaced_text)


    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if (
            not isinstance(value, str)
            or len(value) != 1
            or value not in string.ascii_lowercase
        ):
            raise TypeError("Character must be a single lowercase letter.")

        self._chars.insert(index, value)


    def remove_character(self, value, start=0, end=None):
        if (
            not isinstance(value, str)
            or len(value) != 1
            or value not in string.ascii_lowercase
        ):
            raise TypeError("Character must be a single lowercase letter.")

        if end is None:
            end = len(self._chars) - 1

        if value not in self._chars[start:end + 1]:
            raise ValueError("Character not found.")

        new_chars = []
        for i, c in enumerate(self._chars):
            if start <= i <= end and c == value:
                continue
            new_chars.append(c)

        self._chars = new_chars


    def return_index(self, substring):
        if (
            not isinstance(substring, str)
        ):
            raise TypeError("The substring must be a string of lowercase letters.")

        for c in substring:
            if c not in string.ascii_lowercase:
                raise TypeError("The substring must be a string of lowercase letters.")

        for i in range(len(self._chars) - len(substring) + 1):
            if "".join(self._chars[i:i + len(substring)]) == substring:
                return i
        return -1


    def rotate(self, positions):
        if not isinstance(positions, int):
            raise TypeError("Positions must be an integer.")

        n = len(self._chars)
        if n == 0:
            return

        positions = positions % n
        self._chars = self._chars[-positions:] + self._chars[:-positions]

    def reverse_substring(self, start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Indices start and end must be integers.")

        if start < 0 or end >= len(self._chars) or start > end:
            raise ValueError("Invalid range.")

        self._chars[start: end + 1] = reversed(self._chars[start: end + 1])

    def sliding_window(self, size, overlap=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        if not isinstance(overlap, int):
            raise TypeError("Overlap must be an integer.")
        if size <= 0:
            raise ValueError("Size must be positive.")
        if overlap < 0 or overlap >= size:
            raise ValueError("Overlap must be between 0 and size - 1.")

        step = size - overlap
        result = []
        i = 0

        while i < size:
            window = "".join(self._chars[i:i + step])
            result.append(window)

            if i + size > len(self._chars):
                break

            i += step

        return result


    def count_frequency(self):
        frequency = {}
        for char in self._chars:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        return frequency

    # two MyString are equal if they have the sum of the ascii code of their characters equal
    def equals(self, other):
        if not isinstance(other, MyString):
            raise TypeError("Can only compare with another MyString instance.")

        sum_self = 0
        sum_other = 0
        for c in self._chars:
            sum_self += ord(c)
        for c in other._chars:
            sum_other += ord(c)

        return sum_self == sum_other



    def __add__(self, other):
        if not isinstance(other, MyString):
            raise TypeError("Can only concatenate lowercase letters")

        return MyString("".join(self._chars) + "".join(other._chars))

    def __mul__(self, other ):
        if not isinstance(other, int):
            raise TypeError("Can only multiply by an integer")
        if other < 0:
            raise ValueError("Cannot multiply by a negative integer")

        return MyString("".join(self._chars) * other)

    def __rmul__(self, other):
        return self.__mul__(other)


    def __len__(self):
        return len(self._chars)
