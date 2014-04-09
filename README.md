Butler
======

##Python Dictionaries and Lists on Steroids

Butler is the missing library that adds _additional_ and _necessary_ features to Python ```dict``` as well as ```list```. It helps you traversing nested lists/dicts better. Butler tries to be closely resemble the cpython dictionary functions, but has got a ton of helper functions


__Butler is NOT python dict 2.0__. It is a helper library that provides a clean API for traversing nested lists and dicts.


__Butler suppresses errors and exceptions.__ Its good as well as bad depends on what you expect from it. Also on the kind of data you are working with. If its a huge document(eg., __JSON__ ) with nullable fields and a lot of multi-level lists, ```Butler``` is designed for you.


##Installation

```
pip install python-butler
```

or you can download the source from https://github.com/atmb4u/butler/ and run

```
python setup.py install
```


##Quick Start  Guide


```python
>>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8],
... 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}  
# define dictionary - can be a parsed output of json.loads or json.load

>>> quick = Butler(data)  # create an instance of Butler with the data

>>> quick.path_exists(['c', 'g', 0, 'k'])  # tells you if the element exists
False
# fetches the value on the path, similar to ```<dict>.get()``` but more featured

>>> quick.get(['c', 'g', 0])
{'h': 8, 'i': 9, 'j': 10}

# it can take an argument called default which is taken as the default value if not found.
>>> quick.get(['c', 'g', 5], default=0)
0
>>> quick.find(['b'])
12
>>> quick.findall(['b'])
[12, 2]
>>> quick.key_exists(['n'])
True

>>> quick.data  # chokes out the object which is being manipulated
{'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8],
... 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}
```


##Key Functions

__get()__ - returns the value at the given path

__path_exists()__ - returns if the specified path exists

__findall()__ - returns a list of values for matching keys

__find()__ - returns the first match for the keys

__key_exists()__ - returns True or False, on the availability of the key anywhere in the document

__data__ - outputs the object which is being manipulated


__path__
========

For dictionaries, path holds the keys for the element and for lists its the index for the element in the list.


##get()
Get the element by specifying path with keys to that value.

	* INPUT: __path__ - a list of keys for the dictionary or list

	* OUTPUT: Returns the corresponding value if found, else None. 
		- No Exception raised

```python
>>> data1 = Butler({"key": "value"})
>>> data1.get(["key"])
'value'
>>> data2 = Butler([1, 2, 4, 5, [10, 20, 30, 40, 50]])
>>> data2.get([4, 3])
40
>>> data2.get([4, 9])

>>> data3 = Butler("Hello world")
>>> data3.get([6])
```


##path_exists()

	* INPUT: list containing path to an expected key

	* OUTPUT: True if found, False if NOT.


```python
>>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 
... 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

>>> quick = Butler(data)

>>> quick.path_exists(['c','g',0,'k'])
False
>>> quick.path_exists(['c','g',0,'j'])
True
```


##findall()
Find all the values with the same key in a multi-level dictionary

	* INPUT: key to be searched in the dictionary

	* OUTPUT: ```list``` of all values with matching keys

```python
>>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 
... 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

>>> quick = Butler(data)

>>> quick.findall('a')
```

##find()
Gets the first value matching the argument key

	*INPUT: key to be searched in the dict or list (list position in case of list)

	*OUTPUT: first result matching the key in the entire dictionary


```python
>>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 
... 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

>>> quick = Butler(data)

>>> quick.find('a')
1
>>> quick.find('e')
5
>>> quick.find('w')
```

##key_exists()

Uses find function to see if the requested key is in the dictionary
Returns: ```True``` or ```False```

```python
>>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 
... 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

>>> quick = Butler(data)

>>> quick.key_exists('a')
True
>>> quick.key_exists('w')
False
```
