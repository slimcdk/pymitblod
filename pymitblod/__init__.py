'''
Init file for pymitblod
'''

from .mitblod import MitBlod
from .institution import Institution, Institutions as _Institutions
from .consts import Genders


# A preinitialized instance of institutions 
Institutions = _Institutions()