'''
All model classes for pymitblod
'''
from __future__ import annotations

from .url import Url


class Institution(object):
    '''
    Class representing an institution.
    '''
    def __init__(self, idx: int, name: str, domain: Url, login_form: dict = None) -> Institution:
        self._domain = domain
        self._idx = idx
        self._name = name
        self._login_form = login_form

    def __repr__(self) -> str:
        return str(self._name)

    def domain(self) -> Url:
        ''' TODO '''
        return self._domain

    def auth_path(self) -> str:
        ''' TODO '''
        return self._domain.join_path("auth").join_path("login")

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

    def __login_form__(self, identification, password) -> dict:
        ''' TODO '''
        if self._login_form:
            return self._login_form
        return {'id': identification, 'password': password}
