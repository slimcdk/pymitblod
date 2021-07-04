'''
Consts for pymitblod
'''
from __future__ import annotations

# from .institution import Institution
from .url import Url
from .institution import Institution
from .gender import Gender



class Enum:

    def get_enum_with(self, value:str):
        for var in vars(self).values():
            if var.__repr__() == value: return var

    def list(self):
        return [str(inst) for inst in vars(self).values()]

    def dict(self):
        return vars(self)



class GendersEnum(Enum):

    def __init__(self) -> None:
        super().__init__()
        self.MALE = Gender(
            id           = 0,
            name         = "male", 
            blood_volume_ml_lambda = lambda a,w,h: (1486 * (w**0.425 * h**0.725) * 0.007184) - 825 + 1578 * (w**0.425 * h**0.725 * 0.007184)
        )
        self.FEMALE = Gender(
            id           = 1,
            name         = "female",
            blood_volume_ml_lambda = lambda a,w,h: 1.06 * a + (822 * (w**0.425 * h**0.725 * 0.007184)) + 1395 * (w**0.425 * h**0.725 * 0.007184)
        )

class InstitutionsEnum(Enum):

    def __init__(self) -> None:
        super().__init__()
        self.REGION_SYDDANMARK = Institution(
            id                  = 0,
            name                = "Region Syddanmark", 
            domain              = Url("blodtapning.regionsyddanmark.dk"),
            #login_form_lambda   = lambda id, pass: {'id':id, 'password':pass}
        )
        self.REGION_MIDTJYLLAND = Institution(
            id                  = 1,
            name                = "Region Midtjylland", 
            domain              = Url("bloddonor.rm.dk"),
            #login_form_lambda   = lambda id, pass: {'id':id, 'password':pass}
        )


# A preinitialized instances 
Institutions = InstitutionsEnum()
Genders = GendersEnum()
