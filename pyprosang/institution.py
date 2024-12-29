'''
All model classes for pyprosang
'''
from __future__ import annotations

from .url import Url


class Institution(object):
    '''
    Class representing an institution.
    '''
    def __init__(self, idx:int, name:str, domain:Url, login_form:dict = None) -> Institution:
        self._domain = domain
        self._idx = idx
        self._name = name
        self._login_form = login_form

    def __repr__(self) -> str:
        return str(self._name)

    def __str__(self) -> str:
        return str(self._name)

    def domain(self) -> Url:
        ''' TODO '''
        return self._domain

    def api_translations_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("api").join_path("translations")


    # def auth_path(self) -> str:
    #     ''' TODO '''
    #     return self._domain.join_path("auth").join_path("login")

    def api_login_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("api").join_path("auth").join_path("login")

    def api_login_code_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("api").join_path("auth").join_path("login").join_path("step-2")

    def homepage_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("startpage")

    def upcoming_booking_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("booking").join_path("get-coming-appointments")

    def donations_history_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("tableData").join_path("Donations")

    def messages_history_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("tableData").join_path("DonorMessages")

    def __login_form__(self, identification:str, password:str) -> dict:
        ''' TODO '''
        if self._login_form:
            return self._login_form
        return {'id': identification, 'password': password}
    
    def __login_code_form__(self, code:str) -> dict:
        ''' TODO '''
        return {'password2': code}
