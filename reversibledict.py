import collections

class ReversibleDict(collections.MutableMapping):
	"""A dictionary that allows a reverse mapping from values back to keys"""

	def __init__(self, *args, **kwargs):
		self.store = {}
		self.reverse_store = collections.defaultdict(list)
        self.reverse_as_list = kwargs.pop('reverse_as_list', False)
		self.reverse_as_list_if_none = kwargs.pop('reverse_as_list_if_none', False)

		self.update(dict(*args, **kwargs))

	def __getitem__(self, key):
		return self.store[key]

	def __setitem__(self, key, value):
		self.store[key] = value
		self.reverse_store[self.__valuehash__(value)].append(key)

	def __delitem__(self, key):
		value_hash = self.__valuehash__(self.store[key])

		if (len(self.reverse_store[value_hash]) == 1):
			del self.reverse_store[value_hash]

		del self.store[key]

	def key_for_value(self, value):
		value_hash = self.__valuehash__(value)

		keys = self.reverse_store[value_hash]

		if (len(keys) == 1):
			return keys if self.reverse_as_list else keys[0]
		elif (len(keys) > 1):
			return keys
		else:
			return [] if self.reverse_as_list or self.reverse_as_list_if_none else None

	def __iter__(self):
		return iter(self.store)

	def __len__(self):
		return len(self.store)

	def __valuehash__(self, value):
		return hash(value) if isinstance(value, collections.Hashable) else hash(value.__str__())

	def __str__(self):
		return self.store.__str__()

	def __repr__(self):
		return self.store.__repr__()

	def __unicode__(self):
		return self.store.__unicode__()
