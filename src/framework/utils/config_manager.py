from src.framework.utils.data_utils import JsonUtils


class ConfigManager:
	__CONFIG_FILE = '../project/resources/config.json'
	
	@classmethod
	def get_config(cls):
		return JsonUtils.load_json_file(cls.__CONFIG_FILE)
