'''
All model classes for pymitblod
'''
from __future__ import annotations

import requests
from datetime import datetime
from .institution import Institution
from .consts import Institutions

class MitBlodUser:
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

    
    def institution(self) -> Institution:
        return self._institution


    def id(self) -> str:
        return self._identification

    def partial_id(self) -> str:
        return self._identification[0:6]


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


    def cookies_dict(self) -> dict:
        return self._cookies.get_dict()


    def active_login_cookies(self) -> dict:
        self.login()
        return self.cookies_dict()
        
