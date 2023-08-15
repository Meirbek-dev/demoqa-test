from selenium.webdriver.common.by import By

from src.framework.custom_elements.button import Button
from src.framework.custom_elements.input import Input
from src.framework.page_forms.base_form import BaseForm
from src.project.models.user import User


class RegistrationForm(BaseForm):
    __REGISTRATION_FORM_PAGE_NAME = 'Registration Form'

    def __init__(self):
        super().__init__((By.ID, 'registration-form-modal'), self.__REGISTRATION_FORM_PAGE_NAME)
        self.__first_name_field = Input(
            (By.ID, 'firstName'), self.__REGISTRATION_FORM_PAGE_NAME + ' <first_name_input>'
        )
        self.__last_name_field = Input(
            (By.ID, "lastName"), self.__REGISTRATION_FORM_PAGE_NAME + ' <last_name_input>'
        )
        self.__email_field = Input(
            (By.ID, 'userEmail'), self.__REGISTRATION_FORM_PAGE_NAME + ' <email_input>'
        )
        self.__age_field = Input(
            (By.ID, 'age'), self.__REGISTRATION_FORM_PAGE_NAME + ' <age_input>'
        )
        self.__salary_field = Input(
            (By.ID, 'salary'), self.__REGISTRATION_FORM_PAGE_NAME + ' <salary_input>'
        )
        self.__department_field = Input(
            (By.ID, 'department'), self.__REGISTRATION_FORM_PAGE_NAME + ' <department_input>'
        )
        self.__submit_button = Button(
            (By.ID, 'submit'), self.__REGISTRATION_FORM_PAGE_NAME + ' <submit_btn>'
        )

    def enter_first_name(self, first_name: str):
        self.__first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str):
        self.__last_name_field.send_keys(last_name)

    def enter_email(self, email: str):
        self.__email_field.send_keys(email)

    def enter_age(self, age: int):
        self.__age_field.send_keys(age)

    def enter_salary(self, salary: int):
        self.__salary_field.send_keys(salary)

    def enter_department(self, department: str):
        self.__department_field.send_keys(department)

    def click_submit_btn(self):
        self.__submit_button.click()

    def register_user(self, user: User):
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.enter_age(user.age)
        self.enter_salary(user.salary)
        self.enter_department(user.department)
        self.click_submit_btn()
