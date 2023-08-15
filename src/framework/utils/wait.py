from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.framework.driver.driver import Driver
from src.framework.utils.config_manager import ConfigManager


class Wait:
	__WAIT_TIME = ConfigManager.get_config()["driverSettings"]["timeouts"]["timeoutExplicit"]
	__ALERT_WAIT_TIME = ConfigManager.get_config()["driverSettings"]["timeouts"]["timeoutForAlert"]
	
	@staticmethod
	def until_elem_is_visible(loc):
		return WebDriverWait(Driver.get_driver(), Wait.__WAIT_TIME).until(EC.visibility_of_element_located(loc))
	
	@staticmethod
	def until_all_elems_are_visible(loc):
		return WebDriverWait(Driver.get_driver(), Wait.__WAIT_TIME).until(EC.visibility_of_all_elements_located(loc))
	
	@staticmethod
	def until_elem_is_clickable(loc):
		return WebDriverWait(Driver.get_driver(), Wait.__WAIT_TIME).until(EC.element_to_be_clickable(loc))
	
	@staticmethod
	def until_alert_is_present():
		return WebDriverWait(Driver.get_driver(), Wait.__ALERT_WAIT_TIME).until(EC.alert_is_present())
