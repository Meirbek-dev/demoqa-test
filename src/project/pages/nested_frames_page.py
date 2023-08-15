from selenium.webdriver.common.by import By

from src.framework.custom_elements.label import Label
from src.framework.driver.driver import Driver
from src.framework.page_forms.base_form import BaseForm
from src.framework.utils.wait import Wait


class NestedFramesPage(BaseForm):
	__NESTED_FRAMES_PAGE_NAME = 'Nested Frames'
	__NESTED_FRAMES_PAGE_PARENT_FRAME_ID = "frame1"
	__NESTED_FRAMES_PAGE_CHILD_FRAME_LOC = (By.XPATH, "//iframe[contains(@srcdoc,'Child')]")


	def __init__(self):
		super().__init__((By.XPATH, '//*[@class="main-header"]'), self.__NESTED_FRAMES_PAGE_NAME)
		self.__nested_frames_page_parent_frame_text = Label(
				(By.XPATH, "(/html/body)[1]"), self.__NESTED_FRAMES_PAGE_NAME + ' <parent_frame_text>'
				)
		self.__nested_frames_child_frame_text = Label(
				(By.XPATH, "/html/body/p"), self.__NESTED_FRAMES_PAGE_NAME + ' <child_frame_text>'
				)

	def switch_to_parent_frame(self):
		Driver.switch_to_frame(self.__NESTED_FRAMES_PAGE_PARENT_FRAME_ID)
		
	def switch_to_child_frame(self):
		Driver.switch_to_frame(Wait.until_elem_is_visible(self.__NESTED_FRAMES_PAGE_CHILD_FRAME_LOC))

	def get_parent_frame_text(self):
		return self.__nested_frames_page_parent_frame_text.get_text()

	def get_child_frame_text(self):
		return self.__nested_frames_child_frame_text.get_text()
