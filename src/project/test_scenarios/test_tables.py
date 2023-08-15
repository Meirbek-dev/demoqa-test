import pytest

from src.framework.utils.custom_asserts import CustomAsserts
from src.framework.utils.logger import Logger
from src.project.models.user import User
from src.project.pages.main_page import MainPage
from src.project.pages.registration_form import RegistrationForm
from src.project.pages.sidebar import Sidebar
from src.project.pages.web_tables_page import WebTablesPage


@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize(
	"user_from_json",
	[User.instantiate_from_json(user_num=1),
	 User.instantiate_from_json(user_num=2)]
)
class TestTables:
	@staticmethod
	def test_tables(user_from_json):
		Logger.info('~~~Test scenario "Tables" is running.')
		
		main_page = MainPage()
		assert main_page.is_open(), "Main page is not open"
		main_page.click_elements_btn()
		
		sidebar = Sidebar()
		sidebar.click_web_tables_btn()
		
		web_tables_page = WebTablesPage()
		assert web_tables_page.is_open(), "Web tables page is not open"
		
		web_tables_page.click_add_btn()
		
		registration_form = RegistrationForm()
		assert registration_form.is_open(), "Registration form is not open"
		
		registration_form.register_user(user_from_json)
		
		user_from_table = web_tables_page.instantiate_user_from_table(user_num=4)
		
		CustomAsserts.assert_objects_are_equal(
			user_from_json,
			user_from_table,
			message=f"{user_from_json} data does not match {user_from_table}"
		)
		
		web_tables_page.click_delete_btn(4)
		empty_user_from_table = web_tables_page.instantiate_user_from_table(user_num=4)
		assert User.is_empty(empty_user_from_table)
