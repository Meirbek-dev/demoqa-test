import pytest

from src.framework.driver.driver import Driver
from src.framework.utils.custom_asserts import CustomAsserts
from src.framework.utils.logger import Logger
from src.project.pages.frames_page import FramesPage
from src.project.pages.main_page import MainPage
from src.project.pages.nested_frames_page import NestedFramesPage
from src.project.pages.sidebar import Sidebar


@pytest.mark.usefixtures("setup")
class TestIFrame:

	@staticmethod
	def test_iframe(request):
		Logger.info('~~~Test scenario "Iframe" is running.')

		main_page = MainPage()
		assert main_page.is_open(), "Main page is not open"
		main_page.click_alerts_frame_windows_btn()

		sidebar = Sidebar()
		sidebar.click_nested_frames_btn()

		nested_frames_page = NestedFramesPage()
		assert nested_frames_page.is_open(), "Nested frames page is not open"
		nested_frames_page.switch_to_parent_frame()
		CustomAsserts.assert_text_is_equal(
			nested_frames_page.get_parent_frame_text(),
			request.cls.test_data["parent_frame_text"],
			message=f"Parent frame text is not {request.cls.test_data['parent_frame_text']}, "
			        f"it is {nested_frames_page.get_parent_frame_text()}"
		)
		nested_frames_page.switch_to_child_frame()
		CustomAsserts.assert_text_is_equal(
			nested_frames_page.get_child_frame_text(),
			request.cls.test_data["child_frame_text"],
			message=f"Child frame text is not {request.cls.test_data['child_frame_text']}, "
			        f"it is {nested_frames_page.get_child_frame_text()}"
		)

		Driver.switch_to_default_frame()

		sidebar.click_frames_btn()
		frames_page = FramesPage()
		assert frames_page.is_open(), "Frames page is not open"
		frames_page.switch_to_upper_frame()
		upper_frame_text = frames_page.get_upper_frame_text()
		Driver.switch_to_default_frame()
		frames_page.switch_to_lower_frame()
		lower_frame_text = frames_page.get_lower_frame_text()
		CustomAsserts.assert_text_is_equal(
			upper_frame_text,
			lower_frame_text,
			message=f"Upper frame and lower frame texts are not equal.\n"
			        f"Upper frame text: {upper_frame_text}.\n"
			        f"Lower frame text: {lower_frame_text}"
		)
