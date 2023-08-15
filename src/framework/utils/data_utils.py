from json import load


class JsonUtils:

	@staticmethod
	def load_json_file(file):
		with open(file) as f:
			return load(f)
