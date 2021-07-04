'''
All model classes for pymitblod
'''
from __future__ import annotations

from .gender import Gender


class Person:
    '''
    Class representing a person.
    '''

    def __init__(
        self, name:str, 
        age:float=None, 
        gender:Gender=None, 
        weight:float=None, 
        height:float=None
    ) -> Person:
        self._name:str = name
        self._height:float = height
        self._weight:float = weight
        self._age:float = age
        self._gender:Gender = gender


    def name(self) -> str:
        return self._name


    def age(self) -> float:
        return self._age


    def weight(self) -> float:
        return self._weight


    def height(self) -> float:
        return self._height


    def gender(self) -> Gender:
        return self._gender