'''
Consts for pymitblod
'''

from .models import Institution



class Institutions():

    def __init__(self) -> None:
        self.REGION_SYDDANMARK = Institution("Region Syddanmark", "blodtapning.regionsyddanmark.dk")
        self.REGION_MIDTJYLLAND = Institution("Region Midtjylland", "bloddonor.rm.dk")

    def __repr__(self) -> str:
        return str(vars(self))

    def list(self):
        return list(vars(self).values())
