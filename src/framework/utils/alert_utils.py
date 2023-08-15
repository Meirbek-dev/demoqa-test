from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert

from src.framework.driver.driver import Driver
from src.framework.utils.logger import Logger
from src.framework.utils.wait import Wait


class AlertUtils:
	
	@staticmethod
	def is_present():
		try:
			Wait.until_alert_is_present()
		except TimeoutException:
			Logger.warning("~~~alert is not present")
			return False
		return True
	
	@staticmethod
	def get_text_from_alert():
		return Alert(Driver.get_driver()).text
	
	@staticmethod
	def accept():
		Alert(Driver.get_driver()).accept()
	
	@staticmethod
	def send_keys_to_prompt(text):
		alert = Driver.get_driver().switch_to.alert
		alert.send_keys(text)
		alert.accept()
