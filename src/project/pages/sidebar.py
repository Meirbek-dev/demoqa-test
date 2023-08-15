from selenium.webdriver.common.by import By

from src.framework.custom_elements.button import Button
from src.framework.page_forms.base_form import BaseForm


class Sidebar(BaseForm):
	__SIDEBAR_NAME = 'Sidebar'

	def __init__(self):
		super().__init__((By.CLASS_NAME, 'left-pannel'), self.__SIDEBAR_NAME)
		self.__sidebar_browser_windows_btn = Button(
				(By.XPATH, '//span[text()="Browser Windows"]'), self.__SIDEBAR_NAME + ' <browser_windows_btn>'
				)
		self.__sidebar_alerts_btn = Button(
				(By.XPATH, '//span[text()="Alerts"]//parent::li'), self.__SIDEBAR_NAME + ' <alerts_btn>'
				)
		self.__sidebar_frames_btn = Button(
				(By.XPATH, '//span[text()="Frames"]'), self.__SIDEBAR_NAME + ' <frames_btn>'
				)
		self.__sidebar_nested_frames_btn = Button(
				(By.XPATH, '//span[text()="Nested Frames"]'), self.__SIDEBAR_NAME + ' <nested_frames_btn>'
				)
		self.__sidebar_elements_btn = Button(
				(By.XPATH, '//div[text()="Elements"]'), self.__SIDEBAR_NAME + ' <elements_btn>'
				)
		self.__sidebar_web_tables_btn = Button(
				(By.XPATH, '//span[text()="Web Tables"]'), self.__SIDEBAR_NAME + ' <web_tables_btn>'
				)
		self.__sidebar_links_btn = Button(
				(By.XPATH, '//span[text()="Links"]'), self.__SIDEBAR_NAME + ' <links_btn>'
				)

	def click_browser_windows_btn(self):
		self.__sidebar_browser_windows_btn.click()

	def click_alerts_btn(self):
		self.__sidebar_alerts_btn.click()

	def click_frames_btn(self):
		self.__sidebar_frames_btn.click()

	def click_nested_frames_btn(self):
		self.__sidebar_nested_frames_btn.click()

	def click_elements_btn(self):
		self.__sidebar_elements_btn.click()

	def click_web_tables_btn(self):
		self.__sidebar_web_tables_btn.click()

	def click_links_btn(self):
		self.__sidebar_links_btn.click()
