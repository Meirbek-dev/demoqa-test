from src.framework.custom_elements.base_element import BaseElement
from src.framework.utils.wait import Wait


class Input(BaseElement):
	
	def send_keys(self, text: str, clear_field: bool = True):
		element = Wait.until_elem_is_visible(self.loc)
		if clear_field:
			element.clear()
		element.send_keys(text)
