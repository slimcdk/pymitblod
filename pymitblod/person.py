'''
All model classes for pymitblod
'''

from .consts import Genders
from .utils import *


class Person:
    '''
    Class representing a person.
    '''

    def __init__(self, name:str, age:float=None, gender:Genders=None, weight:float=None, height:float=None):
        self._name:str = name
        self._height:float = height
        self._weight:float = weight
        self._age:float = age
        self._gender:Genders = gender

    def name(self) -> str:
        return self._name
    
    def age(self) -> int:
        return self._age
    
    def gender(self) -> Genders:
        return self._gender
    
    def weight(self) -> float:
        return self._weight
    
    def height(self) -> int:
        return self._height
    
