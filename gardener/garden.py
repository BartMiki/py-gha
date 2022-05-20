from collections import defaultdict
from gardener.plantable import Plantable


class Garden(list[Plantable]):

    def plant(self, plantable: type[Plantable]):
        self.append(plantable.planted())

    def forward_day(self):
        for plant in self:
            plant.age += 1

    def statistics(self) -> dict[str, dict[str, int]]:
        states_dict = defaultdict(lambda: defaultdict(int))
        for plant in self:
            states_dict[plant.state][plant.name] += 1
        
        return states_dict