from selenium.webdriver.common.by import By

from src.framework.custom_elements.base_element import BaseElement
from src.framework.page_forms.base_form import BaseForm


class LinksPage(BaseForm):
	__LINKS_PAGE_NAME = 'Links'

	def __init__(self):
		super().__init__((By.XPATH, '//*[@class="main-header"]'), self.__LINKS_PAGE_NAME)
		self.__links_page_home_anchor = BaseElement((By.ID, "simpleLink"), self.__LINKS_PAGE_NAME + ' <home_anchor>')

	def click_home_anchor(self):
		self.__links_page_home_anchor.click()
