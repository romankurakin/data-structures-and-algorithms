from data_structures_and_algorithms.add import add


def test_add():
    assert add(2, 3) == 5
    assert add("space", "ship") == "spaceship"
