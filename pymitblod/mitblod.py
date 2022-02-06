'''
Primary public API module for pymitblod.
'''

from __future__ import annotations

import requests
import logging
from datetime import datetime
from bs4 import BeautifulSoup

from .institution import Institution
from .donor import Donor
from .user import MitBlodUser
from .gender import Gender


_LOGGER = logging.getLogger(__name__)


class MitBlod(MitBlodUser, Donor):
    '''
    Primary exported interface for pymitblod API wrapper.
    '''
    def __init__(
        self,
        identification: str,
        password: str,
        institution: Institution,
        name: str,
        birthday: datetime,
        gender: Gender,
        weight: int,
        height: int
    ) -> MitBlod:

        MitBlodUser.__init__(
            self=self,
            identification=identification,
            password=password,
            institution=institution
        )
        Donor.__init__(
            self=self,
            name=name,
            birthday=birthday,
            gender=gender,
            weight=weight,
            height=height,
        )

    def mitblod_name(self) -> str:
        '''Fetches the name of the patient'''
        response = requests.get(
            self.institution().homepage_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return " ".join(soup.find(id="full-name").text.split())  # remove weirdly added spaces and newlines

    def blood_type(self) -> str:
        '''Fetches the bloodtype of the patient'''
        response = requests.get(self.institution().homepage_path().secure(), cookies=self.active_login_cookies())
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find(attrs={"class": "blodtype"}).text.strip()

    def next_bookings(self) -> list:
        '''Fetches the next booking for patient'''
        response = requests.get(
            self.institution().upcoming_booking_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()

        bookings = []
        for d in response.json()["data"]:
            bookings.append({
                "location": {
                    "id": d["location"]["id"] or None,
                    "region": self.institution().__repr__(),
                    "name": d["calendar"]["name"] or None,
                    "area": d["location"]["name"] or None,
                },
                "type": d["donationType"],
                "date": datetime.fromisoformat(d["fromDate"]).isoformat()
            })
        return bookings

    def donations(self) -> list:
        '''Fetches donations history for patient'''
        response = requests.get(
            self.institution().donations_history_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()

        # Map data lists to dicts
        keys = response.json()["data"]["classes"]
        history = []
        for data_row in response.json()["data"]["columns"]:
            history_point = {}
            for idx, value in enumerate(data_row):
                history_point[keys[idx]] = value
                if keys[idx].lower().endswith('date'):
                    history_point[f'{keys[idx]}ISO8601'] = datetime.strptime(value, '%d-%m-%Y').isoformat()
            history.append(history_point)
        return history

    def donations_quantity(self) -> int:
        '''Fetches the amount of donations given by the patient'''
        return len(self.donations())

    def messages(self) -> list:
        '''Fetches all messages sent to patient'''
        response = requests.get(
            self.institution().messages_history_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()

        # Map data lists to dicts
        keys = response.json()["data"]["classes"]
        history = []
        for data_row in response.json()["data"]["columns"]:
            history_point = {}
            for idx, value in enumerate(data_row):
                history_point[keys[idx]] = value
                if keys[idx].lower().endswith('date'):
                    history_point[f'{keys[idx]}ISO8601'] = datetime.strptime(value, '%d-%m-%Y, kl. %H:%M').isoformat()
            history.append(history_point)
        return history
