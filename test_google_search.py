from selene.support.shared import browser
from selene import be, have


def test_search_info_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_info_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fdhfhgnthrjtjhnt2134325').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск не выдает результатов')
