from selenium.webdriver.common.by import By

from src.framework.custom_elements.button import Button
from src.framework.page_forms.base_form import BaseForm


class MainPage(BaseForm):
	__MAINPAGE_NAME = 'mainpage'

	def __init__(self):
		super().__init__((By.CLASS_NAME, "home-content"), self.__MAINPAGE_NAME)
		self.__mainpage_afw_btn = Button((By.XPATH, '//*[text()="Alerts, Frame & Windows"]'), self.__MAINPAGE_NAME + '<alerts_frames_windows_btn>')
		self.__mainpage_elements_btn = Button((By.XPATH, '//*[text()="Elements"]'), self.__MAINPAGE_NAME + '<elements_btn>')

	def click_alerts_frame_windows_btn(self):
		self.__mainpage_afw_btn.click()

	def click_elements_btn(self):
		self.__mainpage_elements_btn.click()
