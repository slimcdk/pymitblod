'''
All model classes for pymitblod
'''

from __future__ import annotations
from typing import Callable


class Gender():
    '''
    Class representing an institution.
    '''
    def __init__(
            self, 
            id:int,
            name:str,
            blood_volume_ml_lambda:Callable[[float, float, float], float],
        ):
        self._id = id
        self._name = name
        self._blood_volume_ml_lambda = blood_volume_ml_lambda


    def __repr__(self) -> str:
        return str(self._name)


    def blood_volume_ml_lambda(self) -> Callable:
        return self._blood_volume_ml_lambda
