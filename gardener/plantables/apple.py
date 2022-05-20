from gardener.plantable import Plantable


class Apple(Plantable):
    harvest_age: int = 10
    rotten_age: int = 20
    name: str = "apple"