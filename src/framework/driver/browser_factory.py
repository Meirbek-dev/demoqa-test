from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.framework.utils.config_manager import ConfigManager


class BrowserFactory:
	@staticmethod
	def get_browser(browser_name: str):
		if browser_name.lower() == 'chrome':
			chrome_options = webdriver.ChromeOptions()
			for argument in ConfigManager.get_config()["driverSettings"]["chrome"]["startArguments"]:
				chrome_options.add_argument(argument)
			chrome_options.add_argument(ConfigManager.get_config()["browserName"])
			browser = webdriver.Chrome(
				options=chrome_options,
				service=ChromeService(ChromeDriverManager().install())
			)
			return browser
		elif browser_name.lower() == 'firefox':
			browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
			browser.maximize_window()
			return browser
		else:
			raise ValueError(f"Browser {browser_name} is not supported")
