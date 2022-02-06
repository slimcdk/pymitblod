'''
All model classes for pymitblod
'''


from __future__ import annotations


class Url:
    '''
    Class representing web addresses.
    '''
    def __init__(self, domain: str) -> Url:
        self._domain = domain.replace("https://", "").replace("http://", "").strip()
        self._paths = self._domain.split('/')

    def __repr__(self) -> str:
        return str(self._domain)

    def secure(self) -> str:
        '''Returns SSL URL'''
        return f"https://{self._domain}"

    def unsecure(self) -> str:
        '''Returns unsecure URL'''
        return f"http://{self._domain}"

    def paths(self) -> str:
        '''Returns a list of paths given with this url'''
        return self._paths

    def join_path(self, path: str = None):
        '''Append path to this URL'''
        return Url(f"{self._domain }/{path}")
