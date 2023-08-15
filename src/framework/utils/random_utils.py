import secrets
import string


class RandomUtils:
	@staticmethod
	def get_random_string(length: int):
		return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(length))
