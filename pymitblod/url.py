'''
All model classes for pymitblod
'''


from __future__ import annotations



class Url:
    '''
    Class representing web addresses.
    '''
    def __init__(self, domain:str):
        self._domain = domain.replace("https://", "").replace("http://", "").strip()
        self._paths = self._domain.split('/')


    def __repr__(self) -> str:
        return str(self._domain)


    def secure(self) -> str:
        return f"https://{self._domain}"


    def unsecure(self) -> str:
        return f"http://{self._domain}"


    def paths(self) -> str:
        return self._paths


    def join_path(self, path:str=None):
        return Url(f"{self._domain }/{path}")

