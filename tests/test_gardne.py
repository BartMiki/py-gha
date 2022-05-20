from gardener.garden import Garden
from gardener.plantables.apple import Apple


def test_empty_garden():
    assert len(Garden().statistics()) == 0


def test_garden_with_one_plant():
    g = Garden()
    g.plant(Apple)
    assert g[0] == Apple(0)