'''
All model classes for pymitblod
'''

class Institution:
    '''
    Class representing an institution.
    '''
    def __init__(self, institution_name, base_domain):
        self._name = institution_name
        self._http_type = "https://"
        self._base_domain = base_domain

    def name(self):
        return self._name

    def base_domain(self):
        return f"{self._http_type}{self._base_domain}"

    def auth_path(self):
        return f"{self.base_domain()}/auth/login"

    def homepage_path(self):
        return f"{self.base_domain()}/startpage"

    def create_form(self, username, password):
        return {'id':username, 'password':password}

    def upcoming_booking_path(self):
        return f"{self.base_domain()}/booking/get-coming-appointments"

    def donations_history_path(self):
        return f"{self.base_domain()}/tableData/Donations"

    def messages_history_path(self):
        return f"{self.base_domain()}/tableData/DonorMessages"
