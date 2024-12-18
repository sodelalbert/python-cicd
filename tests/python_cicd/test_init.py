from python_cicd.add import add


def test_generate_list() -> None:
    import time

    time.sleep(2)
    assert 3 == add(1, 2)
