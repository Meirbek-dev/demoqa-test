from src.framework.utils.data_utils import JsonUtils


class TestDataManager:
	__TEST_DATA_FILE = '../project/resources/test_data.json'
	
	@classmethod
	def get_test_data(cls):
		return JsonUtils.load_json_file(cls.__TEST_DATA_FILE)
