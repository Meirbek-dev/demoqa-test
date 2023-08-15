from src.framework.utils.test_data_manager import TestDataManager


class User:
	def __init__(self, first_name: str, last_name: str, email: str, age: int, salary: int, department: str):
		self.__first_name = first_name
		self.__last_name = last_name
		self.__email = email
		self.__age = age
		self.__salary = salary
		self.__department = department

	@property
	def first_name(self):
		return self.__first_name

	@property
	def last_name(self):
		return self.__last_name

	@property
	def email(self):
		return self.__email

	@property
	def age(self):
		return self.__age

	@property
	def salary(self):
		return self.__salary

	@property
	def department(self):
		return self.__department

	@first_name.setter
	def first_name(self, value):
		self.__first_name = value

	@last_name.setter
	def last_name(self, value):
		self.__last_name = value

	@email.setter
	def email(self, value):
		self.__email = value

	@age.setter
	def age(self, value):
		self.__age = value

	@salary.setter
	def salary(self, value):
		self.__salary = value

	@department.setter
	def department(self, value):
		self.__department = value

	@classmethod
	def get_user_from_json(cls, user_num):
		return TestDataManager().get_test_data()["table_users"][user_num - 1]

	@classmethod
	def instantiate_from_json(cls, user_num: int):
		user_data = cls.get_user_from_json(user_num).values()
		return cls(*user_data)

	@staticmethod
	def is_empty(user_data):
		return all([user_field == " " or -1 for user_field in user_data.__dict__.values()])

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
