from selenium.webdriver.common.by import By

from src.framework.custom_elements.button import Button
from src.framework.page_forms.base_form import BaseForm


class BrowserWindowsPage(BaseForm):
	__WINDOWS_PAGE_NAME = 'Browser Windows'

	def __init__(self):
		super().__init__((By.XPATH, '//*[@class="main-header"]'), self.__WINDOWS_PAGE_NAME)
		self.__windows_page_new_tab_btn = Button(
				(By.ID, 'tabButton'), self.__WINDOWS_PAGE_NAME + ' <new_tab_btn>'
				)

	def click_new_tab_btn(self):
		self.__windows_page_new_tab_btn.click()
