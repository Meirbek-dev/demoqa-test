from selenium.webdriver.common.by import By

from src.framework.custom_elements.button import Button
from src.framework.custom_elements.label import Label
from src.framework.page_forms.base_form import BaseForm
from src.project.models.user import User


class WebTablesPage(BaseForm):
	__TABLES_PAGE_NAME = 'Web Tables'
	
	def __init__(self):
		super().__init__((By.XPATH, '//*[@class="main-header"]'), self.__TABLES_PAGE_NAME)
		self.__tables_page_add_btn = Button(
				(By.ID, 'addNewRecordButton'), self.__TABLES_PAGE_NAME + ' <add_btn>'
				)

	def first_name(self, user_num):
		return Label(
				(By.XPATH, f'(//div[@role="row"])[{user_num + 1}]/child::div[1]'),
				self.__TABLES_PAGE_NAME + ' <first_name>'
				)

	def last_name(self, user_num):
		return Label(
				(By.XPATH, f'(//div[@role="row"])[{user_num + 1}]/child::div[2]'),
				self.__TABLES_PAGE_NAME + ' <last_name>'
				)

	def age(self, user_num):
		return Label(
				(By.XPATH, f'(//div[@role="row"])[{user_num + 1}]/child::div[3]'), self.__TABLES_PAGE_NAME + ' <age>'
				)

	def email(self, user_num):
		return Label(
				(By.XPATH, f'(//div[@role="row"])[{user_num + 1}]/child::div[4]'), self.__TABLES_PAGE_NAME + ' <email>'
				)

	def salary(self, user_num):
		return Label(
				(By.XPATH, f'(//div[@role="row"])[{user_num + 1}]/child::div[5]'), self.__TABLES_PAGE_NAME + ' <salary>'
				)

	def department(self, user_num):
		return Label(
				(By.XPATH, f'(//div[@role="row"])[{user_num + 1}]/child::div[6]'),
				self.__TABLES_PAGE_NAME + ' <department>'
				)

	def delete_btn(self, user_num):
		return Label(
				(By.ID, f'delete-record-{user_num}'), self.__TABLES_PAGE_NAME + ' <delete_btn>'
				)

	def click_add_btn(self):
		self.__tables_page_add_btn.click()

	def click_delete_btn(self, user_num):
		self.delete_btn(user_num).click()

	def get_first_name(self, user_num):
		return self.first_name(user_num).get_text()

	def get_last_name(self, user_num):
		return self.last_name(user_num).get_text()

	def get_email(self, user_num):
		return self.email(user_num).get_text()

	def get_age(self, user_num):
		age = self.age(user_num).get_text()
		return -1 if age == " " else int(age)

	def get_salary(self, user_num):
		salary = self.salary(user_num).get_text()
		return -1 if salary == " " else int(salary)

	def get_department(self, user_num):
		return self.department(user_num).get_text()

	def instantiate_user_from_table(self, user_num: int):
		return User(
				first_name=self.get_first_name(user_num),
				last_name=self.get_last_name(user_num),
				age=self.get_age(user_num),
				email=self.get_email(user_num),
				salary=self.get_salary(user_num),
				department=self.get_department(user_num)
				)
