import pytest


def test_firstProgram():
    print("Hello")


@pytest.mark.smoke
def test_secondProgram():
    print("Hello Sunanda")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
