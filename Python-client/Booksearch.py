
# -*- coding: utf-8 -*-
import os
import unittest

from time import sleep


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Booksearch(unittest.TestCase):


    def setUp(self):
   # Setup for the test
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'test'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'/Users/password_specup/Desktop/BookSearch/BookSearch.apk'))
        desired_caps['appPackage'] = 'com.hanmo.booksearchapp'
        desired_caps['appActivity'] = 'ui.search.BookSearchActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def tearDown(self):
      # "Tear down the test"
       self.driver.quit()



    def test_search_field(self):
       #네트워크 비 활성 상태에서 책 검색
       #네트워크 활성 상태에서 책 검색

        self.driver.set_network_connection(0)
        print("network status " + str(self.driver.network_connection))

        bookname = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText')
        bookname.click()
        bookname.send_keys('java')

        searchbutton = self.driver.find_element_by_id('com.hanmo.booksearchapp:id/searchButton')
        searchbutton.click()
        print('버튼클릭성공')
        sleep(2)

        self.driver.back()

        self.driver.set_network_connection(4)

        print("network status " + str (self.driver.network_connection))
        sleep(2)

        bookname = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText')
        bookname.click ()
        bookname.send_keys('pyn')

        searchbutton = self.driver.find_element_by_id('com.hanmo.booksearchapp:id/searchButton')
        searchbutton.click()
        print('버튼클릭성공')


        bookname = self.driver.find_element_by_xpath ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText')
        bookname.click()
        bookname.send_keys('python')

        searchbutton = self.driver.find_element_by_id('com.hanmo.booksearchapp:id/searchButton')
        searchbutton.click()


        self.driver.hide_keyboard()

        bookList = self.driver.find_element_by_id('com.hanmo.booksearchapp:id/bookList')
        action = TouchAction(self.driver)
        action.press(bookList, 999, 1413).wait(2000).move_to(bookList, 999, 514).release().perform()
        sleep(1)
# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Booksearch)

    unittest.TextTestRunner(verbosity=2).run(suite)