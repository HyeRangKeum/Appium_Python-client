
# -*- coding: utf-8 -*-
import os
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Todo(unittest.TestCase):


    def setUp(self):
   # Setup for the test
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'test'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'/Users/password_specup/Desktop/Todo/app-mock-debug.apk'))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
      # "Tear down the test"
       self.driver.quit()



    def test_search_field(self):
        number = 3
        j=0
        i = 1
        while(i < number):
            i += 1
            while (j < number) :
                j += 1
                plusbutoon = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/fab_add_task')
                plusbutoon.click ()
                print('버튼클릭성공')
                sleep(2)

                titlename = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]')
                titlename.click()
                titlename.send_keys('todo(i)')
                self.driver.hide_keyboard()

                text = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/add_task_description')
                text.send_keys('todo todotodotodotodo')
                text.click()

                self.driver.hide_keyboard()

                finishbutton = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/fab_edit_task_done')
                finishbutton.click()
                print('일정등록 완료')


            checkbox = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/complete')
            checkbox.click()

            menubutton = self.driver.find_element_by_accessibility_id('More options')
            menubutton.click()

            delete = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
            delete.click()




# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Todo)

    unittest.TextTestRunner(verbosity=2).run(suite)