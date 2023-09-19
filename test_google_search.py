import pytest
from selene.support.shared import browser
from selene import be, have


def test_search_info_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('oriented Web UI browser test in Python'))
