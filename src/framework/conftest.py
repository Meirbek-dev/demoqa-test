import pytest

from src.framework.driver.driver import Driver
from src.framework.utils.config_manager import ConfigManager
from src.framework.utils.test_data_manager import TestDataManager

@pytest.fixture()
def setup(request):
	request.cls.test_data = TestDataManager.get_test_data()
	main_page = ConfigManager.get_config()["startPageURL"]
	Driver()
	Driver.go_to(main_page)
	yield request.cls.test_data
	Driver.quit()
