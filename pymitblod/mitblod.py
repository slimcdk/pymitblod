'''
Primary public API module for pymitblod.
'''
import requests
import logging
from datetime import datetime
from bs4 import BeautifulSoup
from requests import cookies


from .institution import Institution
from .donor import Donor
from .user import User

from .consts import Genders



_LOGGER = logging.getLogger(__name__)



class MitBlod(User, Donor):
    '''
    Primary exported interface for pymitblod API wrapper.
    '''

    def __init__(self, identification, password, institution, name=None, age=None, gender:Genders=None, weight=None, height=None):
        User.__init__(self=self, identification=identification, password=password, institution=institution)
        Donor.__init__(self=self, name=name, age=age, gender=gender, weight=weight, height=height)
        self._institution = institution


    def institution(self) -> Institution:
        return self._institution


    def name(self):
        if self._name is not None: return self._name
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


    def next_booking(self) -> list:
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
                    "region": self.institution().name() or None,
                    "area": d["calendar"]["name"] or None,
                    "location": d["location"]["name"] or None,
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
                "hb": d[1] or None,
                "blodtryk": d[2] or None,
                "covid_ab": d[3] or None,
                "puls": d[4] or None,
                "tappemåde": d[5] or None
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
