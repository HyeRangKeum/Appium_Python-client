
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
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'/Users/leehanmo/Desktop/todo/app-mock-debug.apk'))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
      # "Tear down the test"
       self.driver.quit()



    def test_search_field(self):
        number = 1
        j=0
        i = 0
        while(i < number):
            i += 1
            while (j < number) :
                j += 1
                plusbutoon = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/fab_add_task')
                plusbutoon.click()
                print('버튼클릭성공')
                sleep(2)

                titlename = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]')
                titlename.click()
                titlename.send_keys('todo todo')
                self.driver.hide_keyboard()

                text = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/add_task_description')
                text.send_keys('todo contents input test ')
                text.click()

                self.driver.hide_keyboard()

                finishbutton = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/fab_edit_task_done')
                finishbutton.click()
                print('일정등록 완료')

            #일정 타이틀 선택
            titleselect = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/title')
            titleselect.click()


            #일정 수정 버튼 선택
            edit = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/fab_edit_task')
            edit.click()

            titlename = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]')
            titlename.click()
            titlename.send_keys('todo')
            self.driver.hide_keyboard ()

            text = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/add_task_description')
            text.send_keys('todo')
            text.click()
            #일정수정완료

            self.driver.hide_keyboard()

            finishbutton = self.driver.find_element_by_id ('com.example.android.architecture.blueprints.tododatabinding.mock:id/fab_edit_task_done')
            finishbutton.click()
            print('일정수정 완료')

            #일정 체크박스 선택
            checkbox = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/complete')
            checkbox.click()

            lockScreenView = self.driver.find_element_by_id('com.example.android.architecture.blueprints.tododatabinding.mock:id/tasksContainer').click()
            self.driver.swipe(12, 768, 559, 768, 1000)

            button2 = self.driver.find_element_by_accessibility_id('Filter')
            button2.click()

            # 메뉴 바 선택
            menubutton = self.driver.find_element_by_accessibility_id('More options')
            menubutton.click()
            #일정 삭제 버튼
            delete = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
            delete.click()
            sleep(5)



# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Todo)

    unittest.TextTestRunner(verbosity=2).run(suite)