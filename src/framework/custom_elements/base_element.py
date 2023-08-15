from src.framework.driver.driver import Driver
from src.framework.utils.logger import Logger
from src.framework.utils.wait import Wait


class BaseElement:
	
	def __init__(self, loc, name):
		self.loc = loc
		self.name = name
	
	def click(self):
		Driver.get_driver().execute_script("arguments[0].click();", Wait.until_elem_is_clickable(self.loc))
		Logger.info('~~~JavaScript click script executed')
	
	def get_text(self):
		return Wait.until_elem_is_visible(self.loc).text
