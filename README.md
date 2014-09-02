#ReversibleDict

*~~~ A dictionary being able to perform a reverse lookup ~~~*

##How does it work?
I calculate a hash of the value (or a hash of the value's `__str__` representation for unhashable types - i.e. `lists`) and internally store the reverse mapping, so no linear search through the values if you thought about that.

##What if there is more than 1 value for a key?
I simply return a `list` of all keys that matched. 

##Usage
```
>>> from reversibledict import ReversibleDict
>>> r = ReversibleDict()
>>> r['a'] = 1
>>> r['b'] = 2
>>> r['c'] = 1
>>> r
{'a': 1, 'c': 1, 'b': 2}
>>> r.key_for_value(2)
'b'
>>> r.key_for_value(1)
['a', 'c']
>>> r.key_for_value(666) == None
True
```

It can also deal with unhashable types such as `lists`:

```
>>> from reversibledict import ReversibleDict
>>> r = ReversibleDict()
>>> r['a'] = [1,2,3]
>>> r['b'] = [3,2,1]
>>> r['c'] = [1]
>>> r['d'] = [1,2,3]
>>> r
{'a': [1, 2, 3], 'c': [1], 'b': [3, 2, 1], 'd': [1, 2, 3]}
>>> r.key_for_value([1,2,3])
['a', 'd']
>>> r.key_for_value([3,2,1])
'b'
>>> r.key_for_value([]) == None
True

```

If you don't like the inconsistency that it is returning a `list` if there is more than 1 matching value, `None` if there is no matching value and a scalar if there is exactly 1 matching value then you can do the following:

```
>>> from reversibledict import ReversibleDict
>>> r = ReversibleDict(reverse_as_list=True)
>>> r['a'] = 1
>>> r['b'] = 2
>>> r['c'] = 1
>>> r
{'a': 1, 'c': 1, 'b': 2}
>>> r.key_for_value(2)
['b']
>>> r.key_for_value(1)
['a', 'c']
>>> r.key_for_value(666)
[]
```