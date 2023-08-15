class CustomAsserts:
	@staticmethod
	def assert_text_is_equal(actual_text, expected_text, message: str = None):
		if not message:
			message = f'Text is "{actual_text}", instead of "{expected_text}"'
		assert actual_text.strip() == expected_text.strip(), message
	
	@staticmethod
	def assert_objects_are_equal(first_obj, second_obj, message: str):
		assert first_obj == second_obj, message
