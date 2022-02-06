'''
All model classes for pymitblod
'''
from __future__ import annotations

from datetime import datetime

from .gender import Gender


class Person(object):
    '''
    Class representing a real person.
    '''

    def __init__(
        self, name: str,
        birthday: datetime = None,
        gender: Gender = None,
        weight: float = None,
        height: float = None
    ) -> Person:
        self._name: str = name
        self._height: float = height
        self._weight: float = weight
        self._birthday: datetime = birthday
        self._gender: Gender = gender

    def name(self) -> str:
        '''Returns the name of this person'''
        return self._name

    def birthday(self) -> datetime:
        '''Returns the birthday of this person'''
        return self._birthday

    def age(self) -> float:
        '''Returns the age of this person'''
        seconds_in_year = 365.25*24*60*60
        return (datetime.now() - self._birthday).total_seconds() / seconds_in_year

    def weight(self) -> float:
        '''Returns the weight of this person'''
        return self._weight

    def height(self) -> float:
        '''Returns the height of this person'''
        return self._height

    def gender(self) -> Gender:
        '''Returns the gender of this person'''
        return self._gender
