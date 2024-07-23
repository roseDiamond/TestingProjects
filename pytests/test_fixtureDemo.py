import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_name(setup):
        print("name ios ok")


    def test_fixtureDemo(setup):
        print("hi my name is sun")