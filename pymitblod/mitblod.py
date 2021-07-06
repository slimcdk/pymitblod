'''
Primary public API module for pymitblod.
'''



from __future__ import annotations

import asyncio, requests,logging
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
            identification:str, 
            password:str, 
            institution:Institution, 
            name:str=None,
            age:int=None,
            gender:Gender=None,
            weight:int=None,
            height:int=None
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
            age=age, 
            gender=gender, 
            weight=weight, 
            height=height,
        )


    def mitblod_name(self) -> str:
        response = requests.get(
            self.institution().homepage_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')       
        return " ".join(soup.find(id="full-name").text.split()) # remove weirdly added spaces and newlines
       

    def blood_type(self) -> str:
        response = requests.get(self.institution().homepage_path().secure(), cookies=self.active_login_cookies())
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find(attrs={"class": "blodtype"}).text.strip()


    def next_bookings(self) -> list:
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
        response = requests.get(
            self.institution().donations_history_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()

        history = []
        for d in response.json()["data"]["columns"]:
            history.append({
                "date": datetime.strptime(d[0], '%d-%m-%Y').isoformat(),
                "hemoglobin_level": d[1] or None,
                "blood_pressure": d[2] or None,
                "covid_antibodies": d[3] or None,
                "heart_rate": d[4] or None,
                "tapping_type": d[5] or None
            })
        return history


    def donations_quantity(self) -> int:
        return len(self.donations())


    def messages(self) -> list:
        response = requests.get(
            self.institution().messages_history_path().secure(),
            cookies=self.active_login_cookies()
        )
        response.raise_for_status()
        
        history = []
        for columns in response.json()["data"]["columns"]:
            history.append({
                "date": datetime.strptime(columns[0], '%d-%m-%Y, kl. %H:%M').isoformat(),
                "type": columns[1] or None,
                "message": columns[2] or None
            })
        return history
