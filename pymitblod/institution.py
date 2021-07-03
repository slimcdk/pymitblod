'''
All model classes for pymitblod
'''

from .url import Url




class Institutions():

    def __init__(self) -> None:
        self.REGION_SYDDANMARK = Institution("Region Syddanmark", Url("blodtapning.regionsyddanmark.dk"))
        self.REGION_MIDTJYLLAND = Institution("Region Midtjylland", Url("bloddonor.rm.dk"))

    # def __iter__(self):
    #     return iter(self)

    # def __next__(self):
    #     elements = [str(inst) for inst in vars(self).values()]

    #     if self.iter_index <= len(elements):
    #         self.iter_index += 1
    #         return elements[self.iter_index]
    #     return StopIteration    

    def list(self):
        return [str(inst) for inst in vars(self).values()]

    def dict(self):
        return vars(self)



class Institution():
    '''
    Class representing an institution.
    '''
    def __init__(self, name:str, domain:Url, login_form=None):
        self._domain = domain
        self._name = name
        self._login_form_ = login_form

    def __repr__(self) -> str:
        return str(self._name)

    def domain(self) -> Url:
        return self._domain

    def auth_path(self) -> str:
        return self._domain.join_path("auth").join_path("login")

    def homepage_path(self) -> str:
        return self._domain.join_path("startpage")

    def upcoming_booking_path(self) -> str:
        return self._domain.join_path("booking").join_path("get-coming-appointments")

    def donations_history_path(self) -> str:
        return self._domain.join_path("tableData").join_path("Donations")

    def messages_history_path(self) -> str:
        return self._domain.join_path("tableData").join_path("DonorMessages")

    def __login_form__(self, identification, password) -> dict:
        if self._login_form_: return self._login_form_
        return {'id':identification, 'password':password}