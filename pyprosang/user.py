'''
All model classes for pyprosang
'''
from __future__ import annotations

import requests
from .institution import Institution


class ProSangUser:
    '''
    Class representing a user with login ability.
    '''
    def __init__(self, identity:str, password:str, institution:Institution) -> ProSangUser:
        self._identity: str = identity
        self._password: str = password
        self._institution: Institution = institution
        self._cookies: dict = None
        self._cookies_expires_at = 0
        self._user_info = None
        self._translations = self.__get_translations__()


    def institution(self) -> Institution:
        '''Returns institution of this user'''
        return self._institution

    def full_identity(self) -> str:
        '''Returns full identification (CPR) of this user'''
        return self._identity

    def partial_identity(self) -> str:
        '''Returns first 6 digits of this users identification (CPR)'''
        return self._identity[0:6]

    def request_login(self) -> tuple[bool, dict]:
        '''Request login code for this user. Real login happens when login_code is called. Returns error code. code 0 is success'''
        formdata = self._institution.__login_form__(self._identity, self._password)
        response = requests.post(self.institution().api_login_path().secure(), data=formdata)
        body = response.json()

        if response.status_code == 200 and body.get('success', False) == True:   
            self.cookies(response.cookies)
            return True, response.json()
        return False, response.json().get('replyStatus', response.json())

    
    def login_code(self, code:str) -> requests.status_codes:
        '''Confirmation code recevied from login request'''
        formdata = self._institution.__login_code_form__(code)
        response = requests.post(self.institution().api_login_code_path().secure(), data=formdata)
        self.cookies(response.cookies)

        response = response.json()
        print(response)
        self._user_info = response.get("user")
        
        return response.status_code

    def is_logged_in(self) -> bool:
        return True

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


    def __get_translations__(self) -> dict:
        response = requests.get(self.institution().api_translations_path().secure())           
        return response.json() if response.status_code == 200 else None