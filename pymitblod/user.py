'''
All model classes for pymitblod
'''
from __future__ import annotations

import requests
from datetime import datetime
from .institution import Institution
from .consts import Institutions

class User:
    '''
    Class representing a user with login ability.
    '''
    def __init__(
            self, 
            identification:str, 
            password:str, 
            institution:Institution
        ):
        self._identification:str = identification
        self._password:str = password
        self._institution:Institution = institution
        self._cookies:dict = None
        self._cookies_expires_at:int = 0

    
    def institution(self) -> Institution:
        return self._institution


    def login(self) -> requests.status_codes:
        formdata = self._institution.__login_form__(self._identification, self._password)
        session = requests.post(self.institution().auth_path().secure(), data=formdata)
        session.raise_for_status()
        self.cookies(session.cookies)
        return session.status_code


    def signout(self) -> None:
        self._cookies = None
        self._cookies_expires_at = 0


    def can_login(self) -> bool:
        return self.login() == 200


    def cookies(self, cookies) -> None:
        self._cookies = cookies
        self._set_cookies_expiration()


    def cookies_dict(self) -> dict:
        return self._cookies.get_dict()


    def cookies_expired(self) -> bool:
        return self._cookies_expires_at < datetime.now().timestamp()


    def _set_cookies_expiration(self) -> None:
        if self._cookies is None:
            self._cookies_expires_at = 0
        for cookie in self._cookies:
            if len(cookie.name) == 40: 
                self._cookies_expires_at = int(cookie.expires)
        else:
            self._cookies_expires_at = 0


    def active_login_cookies(self) -> dict:
        if self.cookies_expired():
            self.login()
        return self.cookies_dict()

