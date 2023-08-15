from selenium.webdriver.common.by import By

from src.framework.custom_elements.label import Label
from src.framework.driver.driver import Driver
from src.framework.page_forms.base_form import BaseForm


class FramesPage(BaseForm):
	__FRAMES_PAGE_NAME = 'Nested Frames'
	__FRAMES_PAGE_UPPER_IFRAME_ID = "frame1"
	__FRAMES_PAGE_LOWER_IFRAME_ID = "frame2"

	def __init__(self):
		super().__init__((By.XPATH, '//*[@class="main-header"]'), self.__FRAMES_PAGE_NAME)
		self.__frames_page_upper_iframe_header = Label(
				(By.ID, "sampleHeading"), self.__FRAMES_PAGE_NAME + ' <upper_frame_text>'
				)
		self.__frames_page_lower_iframe_header = Label(
				(By.ID, "sampleHeading"), self.__FRAMES_PAGE_NAME + ' <lower_frame_text>'
				)

	def switch_to_upper_frame(self):
		Driver.switch_to_frame(self.__FRAMES_PAGE_UPPER_IFRAME_ID)

	def switch_to_lower_frame(self):
		Driver.switch_to_frame(self.__FRAMES_PAGE_LOWER_IFRAME_ID)

	def get_upper_frame_text(self):
		return self.__frames_page_upper_iframe_header.get_text()

	def get_lower_frame_text(self):
		return self.__frames_page_lower_iframe_header.get_text()
