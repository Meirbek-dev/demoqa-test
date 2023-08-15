from selenium.webdriver.common.by import By

from src.framework.page_forms.base_form import BaseForm


class NewTabPage(BaseForm):
	
	def __init__(self):
		super().__init__((By.ID, "sampleHeading"), 'New Tab Page')
