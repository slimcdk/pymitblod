'''
All model classes for pymitblod
'''
from __future__ import annotations

from .consts import Genders
from .person import Person
from .utils import *
from .gender import Gender


class Donor(Person):
    
    def __init__(
            self,
            name:str,
            gender:Gender,
            age:float,
            weight:float,
            height:float,
        ) -> Donor:
        Person.__init__(
            self=self, 
            name=name,
            age=age,
            gender=gender,
            weight=weight, 
            height=height
        )


    def blood_volume_ml(self) -> int:
        return self._gender.blood_volume_ml_lambda()(self._age, self._weight, self._height)