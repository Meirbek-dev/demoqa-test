from src.framework.driver.browser_factory import BrowserFactory
from src.framework.utils.config_manager import ConfigManager
from src.framework.utils.singleton import Singleton


class Driver(metaclass=Singleton):
	__driver = None
	
	@staticmethod
	def __init__():
		Driver.__driver = BrowserFactory.get_browser(ConfigManager.get_config()["browserName"])
	
	@staticmethod
	def get_driver():
		return Driver.__driver
	
	@staticmethod
	def go_to(url):
		Driver.get_driver().get(url)
	
	@staticmethod
	def switch_to_frame(frame_name):
		Driver.get_driver().switch_to.frame(frame_name)
	
	@staticmethod
	def switch_to_default_frame():
		Driver.get_driver().switch_to.default_content()
	
	@staticmethod
	def switch_to_alert():
		return Driver.get_driver().switch_to.alert
	
	@staticmethod
	def switch_to_first_tab():
		Driver.get_driver().switch_to.window(Driver.get_driver().window_handles[0])
	
	@staticmethod
	def switch_to_last_tab():
		Driver.get_driver().switch_to.window(Driver.get_driver().window_handles[-1])
	
	@staticmethod
	def close_current_tab():
		Driver.get_driver().close()
	
	@staticmethod
	def quit():
		Driver.get_driver().quit()
		Singleton.instances.pop(Driver)
