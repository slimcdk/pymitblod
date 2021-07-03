'''
All model classes for pymitblod
'''

from .consts import Genders
from .person import Person
from .utils import *



class Donor(Person):
    
    def __init__(self, name:str, age:float, gender:Genders, weight:float, height:float):
        Person.__init__(self=self, name=name, age=age, gender=gender, weight=weight, height=height)

    def blood_volume_ml(self) -> int:
        if self._gender is Genders.MALE:
            return int(male_blood_volume(self._age, self._weight, self._height))
        elif self._gender is Genders.FEMALE:
            return int(female_blood_volume(self._age, self._weight, self._height))
        return None