from jaraco.util import dictlib

class AlwaysStringKeysDict(dictlib.KeyTransformingDict):
	"""
	An implementation of a KeyTransformingDict subclass that always converts
	the keys to strings.
	"""
	@staticmethod
	def key_transform(key):
		return unicode(key)

def test_always_lower_keys_dict():
	"""
	Tests AlwaysLowerKeysDict to ensure KeyTransformingDict works.
	"""
	d = AlwaysStringKeysDict()
	d['farther'] = 'closer'
	d['Lasting'] = 'fleeting'
	d[3] = 'three'
	d[{'a': 1}] = 'a is one'
	assert all(isinstance(key, unicode) for key in d)
	assert "{'a': 1}" in d
	assert 3 in d
	assert d[3] == d['3'] == 'three'
