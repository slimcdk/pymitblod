'''
All model classes for pymitblod
'''
from __future__ import annotations

from datetime import datetime
import math

from .enums import Genders
from .person import Person
from .gender import Gender


# Blood volume calculation methods
# https://pubmed.ncbi.nlm.nih.gov/30252333/

# Method 1
def nadlers_male_blood_volume_ml_lambda(w, h):
    '''TODO'''
    return (0.3669 * h**3) + (0.03219 * w) + 0.6041


def nadlers_female_blood_volume_ml_lambda(w, h):
    '''TODO'''
    return (0.3561 * h**3) + (0.03308 * w) + 0.1833


# Method 2
def lemmens_bernstein_brodsky_blood_volume_ml_lambda(bmi):
    '''TODO'''
    return 70 / math.sqrt(bmi/22)


# Method 3
def weight_height_male_blood_volume_ml_lambda(a, w, h):
    '''TODO'''
    return (1486 * (w**0.425 * h**0.725) * 0.007184) - 825 + 1578 * (w**0.425 * h**0.725 * 0.007184)


def weight_height_female_blood_volume_ml_lambda(a, w, h):
    '''TODO'''
    return 1.06 * a + (822 * (w**0.425 * h**0.725 * 0.007184)) + 1395 * (w**0.425 * h**0.725 * 0.007184)


class Donor(Person):

    '''
    Class representing a doner.
    '''

    def __init__(self, name: str, gender: Gender, birthday: datetime, weight: float, height: float) -> Donor:
        Person.__init__(self=self, name=name, birthday=birthday, gender=gender, weight=weight, height=height)

    def body_mass_index(self) -> float:
        '''Returns the body mass index of this donor'''
        return self._weight / ((self._height/100)**2)

    # https://www.ncbi.nlm.nih.gov/books/NBK278991/table/diet-treatment-obes.table4clas/
    def body_mass_index_class(self) -> float:
        '''Returns the bmi class of this donor'''
        bmi_class = None
        bmi = self.body_mass_index()
        if bmi < 18.5:
            bmi_class = "Underweight"
        elif 18.5 <= bmi < 25:
            bmi_class = "Normal weight"
        elif 25 <= bmi < 30:
            bmi_class = "Overweight"
        elif 30 <= bmi < 35:
            bmi_class = "Obesity Class 1"
        elif 35 <= bmi < 40:
            bmi_class = "Obesity Class 2"
        elif bmi > 40:
            bmi_class = "Extreme Obesity Class 3"
        return bmi_class

    def estimated_blood_volume_ml(self, method: str = "lemmens") -> int:
        '''Return the estimated blood volume of this person'''

        if method.strip() == "random":
            if self._gender == Genders.MALE:
                return weight_height_male_blood_volume_ml_lambda(self.age(), self._weight, self._height)
            elif self._gender == Genders.FEMALE:
                return weight_height_female_blood_volume_ml_lambda(self.age(), self._weight, self._height)

        if method.strip() == "nadlers":
            if self._gender == Genders.MALE:
                return nadlers_male_blood_volume_ml_lambda(self._weight, self._height/100) * 1000
            elif self._gender == Genders.FEMALE:
                return nadlers_female_blood_volume_ml_lambda(self._weight, self._height/100) * 1000

        if method.strip() == "lemmens":
            return lemmens_bernstein_brodsky_blood_volume_ml_lambda(self.body_mass_index()) * 100

        raise ValueError(f'Method {method} not recognized.')
