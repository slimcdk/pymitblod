'''
Primary public API module for pymitblod.
'''
import requests
import logging
from datetime import datetime
from bs4 import BeautifulSoup


_LOGGER = logging.getLogger(__name__)


class MitBlod:
    '''
    Primary exported interface for eloverblik.dk API wrapper.
    '''

    def __init__(self, username, password, institustion):
        self._username = username
        self._password = password
        self._institustion = institustion
        self._cookies = None
        self._session_expires = 0

        self._acquire_cookies()


    def _acquire_cookies(self):
        _LOGGER.debug(f"Requesting access at {self._institustion.name()}")

        if self._session_expires <  datetime.now().timestamp() or self._cookies is None:
            _LOGGER.debug("Refreshing cookies")
            formdata = self._institustion.create_form(self._username, self._password)
            response = requests.post(self._institustion.auth_path(), data=formdata)
            response.raise_for_status()

            # eat cookies
            self._cookies = response.cookies.get_dict()
            for cookie in response.cookies:
                if len(cookie.name) == 40: self._session_expires = int(cookie.expires)

        else:
            _LOGGER.debug("Cookies are still valid")
        return self._cookies


    def _get_data(self, url):
        self._acquire_cookies()

        response = requests.get(url, cookies=self._cookies)
        response.raise_for_status()
        if response.json()["replyStatus"]["status"] != "OK":
            return None
        return response.json()["data"]


    def name(self):
        self._acquire_cookies()
        response = requests.get(self._institustion.homepage_path(), cookies=self._cookies)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')       
        return " ".join(soup.find(id="full-name").text.split()) # remove weirdly added spaces and newlines


    def blood_type(self):
        self._acquire_cookies()
        response = requests.get(self._institustion.homepage_path(), cookies=self._cookies)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find(attrs={"class": "blodtype"}).text.strip()


    def next_booking(self):

        bookings = []
        for d in self._get_data(self._institustion.upcoming_booking_path()):
            bookings.append({
                "location": {
                    "id": d["location"]["id"] or None,
                    "region": self._institustion.name() or None,
                    "area": d["calendar"]["name"] or None,
                    "location": d["location"]["name"] or None,
                },
                "type": d["donationType"],
                "date": datetime.fromisoformat(d["fromDate"]).isoformat()
            })
        return bookings



    def donations(self):
        data = self._get_data(self._institustion.donations_history_path())
        history = []
        for d in data["columns"]:
            history.append({
                "date": datetime.strptime(d[0], '%d-%m-%Y').isoformat(),
                "hb": d[1] or None,
                "blodtryk": d[2] or None,
                "covid_ab": d[3] or None,
                "puls": d[4] or None,
                "tappemåde": d[5] or None
            })
        return history

    def donations_quantity(self):
        return len(self.donations())




    def messages(self):      
        history = []
        for columns in self._get_data(self._institustion.messages_history_path())["columns"]:
            history.append({
                "date": datetime.strptime(columns[0], '%d-%m-%Y, kl. %H:%M').isoformat(),
                "type": columns[1] or None,
                "message": columns[2] or None
            })
        return history
