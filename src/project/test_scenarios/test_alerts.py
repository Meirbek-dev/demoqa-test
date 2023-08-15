import pytest

from src.framework.utils.alert_utils import AlertUtils
from src.framework.utils.custom_asserts import CustomAsserts
from src.framework.utils.logger import Logger
from src.framework.utils.random_utils import RandomUtils
from src.project.pages.alerts_page import AlertsPage
from src.project.pages.main_page import MainPage
from src.project.pages.sidebar import Sidebar


@pytest.mark.usefixtures("setup")
class TestAlerts:
	@staticmethod
	def test_alerts(request):
		Logger.info('~~~Test scenario "Alerts" is running.')
		
		main_page = MainPage()
		assert main_page.is_open(), "Main page is not open"
		main_page.click_alerts_frame_windows_btn()
		
		sidebar = Sidebar()
		sidebar.click_alerts_btn()
		alerts_page = AlertsPage()
		assert alerts_page.is_open(), "Alerts page is not open"
		
		alerts_page.click_alert_btn()
		alert = AlertUtils()
		assert alert.is_present(), "Alert is not present"
		CustomAsserts.assert_text_is_equal(alert.get_text_from_alert(), request.cls.test_data["alert_text"])
		alert.accept()
		assert alert.is_present() is False, "Alert is still present"
		
		alerts_page.click_confirm_box()
		confirm_box = AlertUtils()
		assert confirm_box.is_present(), "Confirm box is not present"
		CustomAsserts.assert_text_is_equal(
				confirm_box.get_text_from_alert(), request.cls.test_data["confirm_box_text"]
				)
		confirm_box.accept()
		assert confirm_box.is_present() is False, "Confirm box is still present"
		CustomAsserts.assert_text_is_equal(
				alerts_page.get_confirm_box_result_text(),
				request.cls.test_data["confirm_box_result_text"]
				)
		
		alerts_page.click_prompt_box()
		prompt_box = AlertUtils()
		assert prompt_box.is_present(), "Prompt box is not present"
		CustomAsserts.assert_text_is_equal(prompt_box.get_text_from_alert(), request.cls.test_data["prompt_text"])
		random_text = RandomUtils.get_random_string(length=15)
		prompt_box.send_keys_to_prompt(random_text)
		assert prompt_box.is_present() is False, "Prompt box is still present"
		CustomAsserts.assert_text_is_equal(alerts_page.get_prompt_box_result_text(), "You entered " + random_text)
