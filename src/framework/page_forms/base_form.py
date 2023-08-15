from src.framework.utils.logger import Logger
from src.framework.utils.wait import Wait


class BaseForm:
	
	def __init__(self, loc, name):
		self.loc = loc
		self.name = name
		Logger.info(f"~~~{self.name} is initialized")
	
	def is_open(self):
		elements = Wait.until_all_elems_are_visible(self.loc)
		if elements:
			Logger.info(f"~~~{self.name} is opened")
		return bool(elements)
