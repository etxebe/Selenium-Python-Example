import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from homepage import HomePage
from locators import *


class OnetWeatherCheck(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        fp = webdriver.FirefoxProfile(r'C:\Users\aeru\AppData\Roaming\Mozilla\Firefox\Profiles\9ypijang.Selenium')
        self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)

    def test_checkHomePage(self):
        homepage = HomePage(self.driver)
        homepage.navigate()
        self.assertEqual(homepage.get_current_url(), homepage.url)
        self.assertEqual(homepage.get_title(), 'Onet.pl')

    def test_checkWeatherTemperatures(self):
        homepage = HomePage(self.driver)
        homepage.navigate()
        homepage.is_page_loaded(HomePageLocators.CHECK_PAGE_LOADED)
        homepage.select_city('Poznań')

        self.assertEqual(homepage.get_text_from_element(*HomePageLocators.WEATHER_NOW), '7°C')
        self.assertEqual(homepage.get_text_from_element(*HomePageLocators.WEATHER_TOMORROW), '10°C')
        self.assertEqual(homepage.get_text_from_element(*HomePageLocators.SELECTED_CITY), 'Warszawa')

    def test_checkWeatherInOtherCity(self):
        homepage = HomePage(self.driver)
        homepage.navigate()
        homepage.is_page_loaded(HomePageLocators.CHECK_PAGE_LOADED)
        homepage.search_for_city('Tczew')

        self.assertEqual(homepage.get_text_from_element(*HomePageLocators.WEATHER_NOW), '7°C')
        self.assertEqual(homepage.get_text_from_element(*HomePageLocators.WEATHER_TOMORROW), '9°C')
        self.assertEqual(homepage.get_text_from_element(*HomePageLocators.SELECTED_CITY), 'Olsztyn')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()