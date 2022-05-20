from __future__ import annotations
from abc import ABC, abstractmethod
from unicodedata import name


GROWING = "growing"
HARVESTABLE = "harvestable"
ROTTEN = "rotten"

class Plantable(ABC):
    harvest_age: int
    rotten_age: int
    name: str

    def __hash__(self) -> int:
        return hash(self.name + str(self.age))

    def __eq__(self, o: object) -> bool:
        return type(self) == type(o) and hash(self) == hash(o)

    def __str__(self) -> str:
        return f"{type(self)}({self.age})"

    def __repr__(self) -> str:
        return str(self)

    def __init__(self, age) -> None:
        self.age = age

    @classmethod
    def planted(cls) -> Plantable:
        return cls(0)

    @property
    def state(self) -> str:
        """ Returns one of: 'growing', 'harvestable', 'rotten' """
        if self.age < self.harvest_age:
            return GROWING
        elif self.harvest_age <= self.age < self.rotten_age:
            return HARVESTABLE
        else:
            return ROTTEN