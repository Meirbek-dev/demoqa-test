from selenium.webdriver.common.by import By

from src.framework.custom_elements.button import Button
from src.framework.custom_elements.label import Label
from src.framework.page_forms.base_form import BaseForm


class AlertsPage(BaseForm):
	__ALERTS_PAGE_NAME = 'Alerts'

	def __init__(self):
		super().__init__((By.XPATH, '//*[@class="main-header"]'), self.__ALERTS_PAGE_NAME)
		self.__alerts_page_alert_btn = Button((By.ID, "alertButton"), self.__ALERTS_PAGE_NAME + '<alert_btn>')
		self.__alerts_page_confirm_box_btn = Button((By.ID, "confirmButton"),
		                                            self.__ALERTS_PAGE_NAME + '<confirm_box_btn>')
		self.__alerts_page_prompt_box_btn = Button((By.ID, "promtButton"),
		                                           self.__ALERTS_PAGE_NAME + '<prompt_box_btn>')
		self.__alerts_page_confirm_box_result = Label((By.ID, "confirmResult"),
		                                              self.__ALERTS_PAGE_NAME + '<confirm_result_text>')
		self.__alerts_page_prompt_box_result = Label((By.ID, 'promptResult'),
		                                             self.__ALERTS_PAGE_NAME + '<prompt_box_result_text>')

	def click_alert_btn(self):
		self.__alerts_page_alert_btn.click()

	def click_confirm_box(self):
		self.__alerts_page_confirm_box_btn.click()

	def click_prompt_box(self):
		self.__alerts_page_prompt_box_btn.click()

	def get_confirm_box_result_text(self):
		return self.__alerts_page_confirm_box_result.get_text()

	def get_prompt_box_result_text(self):
		return self.__alerts_page_prompt_box_result.get_text()
