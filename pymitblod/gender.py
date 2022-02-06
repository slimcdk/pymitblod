'''
All model classes for pymitblod
'''

from __future__ import annotations


class Gender():
    '''
    Class representing an institution.
    '''
    def __init__(self, idx: int, name: str) -> Gender:
        self._idx = idx
        self._name = name

    def __repr__(self) -> str:
        return str(self._name)
