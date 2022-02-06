'''
All model classes for pymitblod
'''
from __future__ import annotations

import requests
from .institution import Institution


class MitBlodUser:
    '''
    Class representing a user with login ability.
    '''
    def __init__(
        self,
        identification: str,
        password: str,
        institution: Institution
    ) -> MitBlodUser:
        self._identification: str = identification
        self._password: str = password
        self._institution: Institution = institution
        self._cookies: dict = None
        self._cookies_expires_at = 0

    def institution(self) -> Institution:
        '''Returns institution of this user'''
        return self._institution

    def full_id(self) -> str:
        '''Returns full identification (CPR) of this user'''
        return self._identification

    def partial_id(self) -> str:
        '''Returns first 6 digits of this users identification (CPR)'''
        return self._identification[0:6]

    def login(self) -> requests.status_codes:
        '''Set active login session cookies on this user'''
        formdata = self._institution.__login_form__(self._identification, self._password)
        session = requests.post(self.institution().auth_path().secure(), data=formdata)
        self.cookies(session.cookies)
        return session.status_code

    def signout(self) -> None:
        '''Clear login cookies'''
        self._cookies = None
        self._cookies_expires_at = 0

    def can_login(self) -> bool:
        '''Check if this user really can login'''
        return self.login() == 200

    def cookies(self, cookies) -> None:
        '''Get the cookies for the current login session'''
        self._cookies = cookies

    def cookies_dict(self) -> dict:
        '''Get the cookies for the current login session as dict'''
        return self._cookies.get_dict()

    def active_login_cookies(self) -> dict:
        '''Log user in and return freshly baked cookies'''
        self.login()
        return self.cookies_dict()
