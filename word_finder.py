class Finder:

	@staticmethod
	def create_char_map(key):
		"""
		Function to create character map of occurrences of each
		charactersss
		:param key: string
		:return:list containing occurrences of each character
		"""
		char_count_list = [0] * 26
		for single_char in key:
			char_count_list[ord(single_char) - 97] += 1
		return char_count_list

	def __create_data_map(self):
		"""
		Function to create map of strings with the
		list of occurrences of each char
		:return:
		"""
		for item in self.__data_list:
			self.__data_map.update({
				item: Finder.create_char_map(item)})

	def __init__(self, data_list):
		self.__data_list = data_list
		self.__data_map = {}
		self.__create_data_map()

	def find(self, key):
		"""
		Function to match if any of the strings have
		same occurrences of characters as in the key provided.
		:param key: key which is to be searched
		:return:
		"""
		found_keys = []
		key_char_map = Finder.create_char_map(key)
		for key, value in self.__data_map.items():
			fail = False
			for i in range(0, 26):
				if key_char_map[i]:
					if value[i] != key_char_map[i]:
						fail = True
						break
			if not fail:
				found_keys.append(key)
		return found_keys


if "__name__" == "__main__":
	f = Finder(['asd', 'asdd', 'fre'])
	print(f.find('sad'))

"""
Assumptions 
1. given character would always be in a-z range.

"""