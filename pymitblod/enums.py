'''
Enums for pymitblod
'''
from __future__ import annotations


# from .institution import Institution
from .url import Url
from .institution import Institution
from .gender import Gender


class Enum:
    '''
    Base class for a enums
    '''

    def get_enum_for(self, value: str):
        '''Search for enum with given value'''
        for var in vars(self).values():
            if var.__repr__() == value:
                return var

    def dict(self):
        '''Return all values as a dict'''
        return vars(self)

    def list(self):
        '''Return all enums as list'''
        return list(self.dict().values())

    def keys(self):
        '''Return all values as a dict'''
        return list(self.dict().keys())


class GenderEnums(Enum):

    '''
    Pre instantiate institutions.
    '''

    def __init__(self) -> GenderEnums:
        self.MALE = Gender(idx=0, name="male")
        self.FEMALE = Gender(idx=1, name="female")

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return "Genders"


class InstitutionEnums(Enum):

    '''
    Pre-instantiate institutions.
    '''

    def __init__(self) -> InstitutionEnums:
        self.REGION_SYDDANMARK = Institution(
            idx=0,
            name="Region Syddanmark",
            domain=Url("blodtapning.regionsyddanmark.dk"),
        )

        self.REGION_MIDTJYLLAND = Institution(
            idx=1,
            name="Region Midtjylland",
            domain=Url("bloddonor.rm.dk"),
        )

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return "Institutions"


# Preinitialized instances.
Institutions = InstitutionEnums()
Genders = GenderEnums()
