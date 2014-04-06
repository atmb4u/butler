Butler - Python Dictionaries and Lists on Steroids
==================================================

Butler is the missing library to add additional and necessary features to Python ```dict``` as well as ```list```. Butler tries to be closely resemble the cpython dictionary functions, but has got a ton of helper functions

__Bulter suppresses errors and exceptions.__ Its good as well as bad depends on what kind of data you are working with. If its a huge document(like __JSON__ ) with nullable fields and a lot of multi-level lists, ```Butler``` is designed for you.

##get()
Get the element by specifying path with keys to that value.
	* INPUT: takes a list of keys for the dictionary or list
	* OUTPUT: Returns the corresponding value if found, else None. - No Exception raised

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
        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
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
        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
        ... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

        >>> quick = Butler(data)

        >>> quick.findall('a')
```

##find()
Gets the first value matching the argument key
	*INPUT: key to be searched in the dict or list (list position in case of list)
	*OUTPUT: first result matching the key in the entire dictionary


```python
        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
        ... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

        >>> quick = Butler(data)

        >>> quick.find('a')
        1
        >>> quick.find('e')
        5
        >>> quick.find('w')
```