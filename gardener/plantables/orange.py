from gardener.plantable import Plantable


class Orange(Plantable):
    harvest_age: int = 15
    rotten_age: int = 17
    name: str = "orange"