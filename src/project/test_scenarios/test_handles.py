import pytest

from src.framework.driver.driver import Driver
from src.framework.utils.logger import Logger
from src.project.pages.browser_windows_page import BrowserWindowsPage
from src.project.pages.links_page import LinksPage
from src.project.pages.main_page import MainPage
from src.project.pages.new_tab_page import NewTabPage
from src.project.pages.sidebar import Sidebar


@pytest.mark.usefixtures("setup")
class TestHandles:
	@staticmethod
	def test_handles():
		Logger.info('~~~Test scenario "Handles" is running.')
		
		main_page = MainPage()
		assert main_page.is_open(), "Main page is not open"
		main_page.click_alerts_frame_windows_btn()
		
		sidebar = Sidebar()
		sidebar.click_browser_windows_btn()
		
		browser_windows_page = BrowserWindowsPage()
		assert browser_windows_page.is_open(), "Browser windows page is not open"
		browser_windows_page.click_new_tab_btn()
		
		Driver.switch_to_last_tab()
		new_tab_page = NewTabPage()
		assert new_tab_page.is_open(), "New tab page is not open"
		Driver.close_current_tab()
		
		Driver.switch_to_first_tab()
		assert browser_windows_page.is_open(), "Browser windows page is not open"
		
		sidebar.click_elements_btn()
		sidebar.click_links_btn()
		
		links_page = LinksPage()
		assert links_page.is_open(), "Links page is not open"
		links_page.click_home_anchor()
		Driver.switch_to_last_tab()
		assert main_page.is_open(), "Main page is not open"
		Driver.switch_to_first_tab()
		assert links_page.is_open(), "Links page is not open"
