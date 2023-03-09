import pytest
from selene import be, have
from selene.support.shared import browser

@pytest.fixture
def browser_settings():
    browser.config.window_width = 2650
    browser.config.window_height = 1440
def test_google_search_positive(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Futurama release date').press_enter()
    browser.element('[id="search"]').should(have.text('Futurama Reboot - All We Know - GIANT FREAKIN ROBOT'))

def test_google_search_negative(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('q3rweqrerw').press_enter()
    browser.element('.card-section').should(have.text('По запросу q3rweqrerw ничего не найдено. '))


