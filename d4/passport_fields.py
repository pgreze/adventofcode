#!/usr/bin/env python3

import re

"""
Run tests with:

>> python3 -m pip install pytest
>> python3 -m pytest passport-checker-v2.py --doctest-modules
"""

__all__ = ("REQUIRED_FIELDS", "FIELD_VALIDATORS")

def is_in_range(min, max):
    """Validate a number between min and max.

    >>> is_in_range(10, 20)("1")
    False
    >>> is_in_range(10, 20)("10")
    True
    >>> is_in_range(10, 20)("20")
    True
    >>> is_in_range(10, 20)("21")
    False
    >>> is_in_range(10, 20)("hi")
    False
    """
    def is_valid(value):
        try:
            return min <= int(value) <= max
        except:
            return False
    return is_valid

def is_valid_height(value: str):
    """Validate a number followed by either cm or in:
    - If cm, the number must be at least 150 and at most 193.
    - If in, the number must be at least 59 and at most 76.

    >>> is_valid_height("60in")
    True
    >>> is_valid_height("190cm")
    True
    >>> is_valid_height("190in")
    False
    >>> is_valid_height("190")
    False
    """
    if value.endswith("cm"):
        return is_in_range(150, 193)(value[:-2])
    elif value.endswith("in"):
        return is_in_range(59, 76)(value[:-2])
    else:
        return False

def is_valid_hair_color(value):
    """Validate a # followed by exactly six characters 0-9 or a-f.

    >>> is_valid_hair_color("#123abc")
    True
    >>> is_valid_hair_color("#123abz")
    False
    >>> is_valid_hair_color("123abc")
    False
    """
    return bool(re.match(r"^#[0-9a-f]{6}$", value))

def is_valid_passport_id(value):
    """Validate a nine-digit number, including leading zeroes.

    >>> is_valid_passport_id("000000001")
    True
    >>> is_valid_passport_id("0123456789")
    False
    """
    return bool(re.match(r"^\d{9}$", value))

FIELD_VALIDATORS = {
    "byr": is_in_range(1920, 2002),
    "iyr": is_in_range(2010, 2020),
    "eyr": is_in_range(2020, 2030),
    "hgt": is_valid_height,
    "hcl": is_valid_hair_color,
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": is_valid_passport_id,
    "cid": lambda x: True,
}

REQUIRED_FIELDS = FIELD_VALIDATORS.keys()
