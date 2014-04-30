import warnings

__version__ = "0.91"
__license__ = "BSD"
__contact__ = "atmb4u at gmail dot com"


class Butler(object):
    def __init__(self, data):
        """
        Initiates with the list or dict object obj
        """
        self.data = data

    def __getitem__(self, path):
        """
        Grab values inside nested dict and list if available, else returns None
        Returns None if looking up in string.
        keys: A list of names or ids
        >>> data1 = Butler({"key": "value"})
        >>> data1.get(["key"])
        'value'
        >>> data2 = Butler([1, 2, 4, 5, [10, 20, 30, 40, 50]])
        >>> data2.__getitem__([4, 3])
        40
        >>> data2.get([4, 9])

        >>> data3 = Butler("Hello world")
        >>> data3.get([6])

        """
        return_obj = self.data
        for key in path:
            if type(return_obj) in [list, dict]:
                return_obj = return_obj[key]
            else:
                return None
        return return_obj

    def get(self, path, default=None):
        """
        Grab values inside nested dict and list if available, else returns None
        Returns None if looking up in string.
        keys: A list of names or ids
        >>> data1 = Butler({"key": "value"})
        >>> data1.get(["key"])
        'value'
        >>> data2 = Butler([1, 2, 4, 5, [10, 20, 30, 40, 50]])
        >>> data2.get([4, 3])
        40
        >>> data2.get([4, 9])

        >>> data3 = Butler("Hello world")
        >>> data3.get([6])

        >>> data2.get([4, 10], default="BLANK")
        'BLANK'
        >>> data2.get([4, 42], 0)
        0
        """
        try:
            return self[path]
        except (LookupError, TypeError):
            warnings.warn("Could not find the requested element", UserWarning)
            return default

    def path_exists(self, path):
        """
        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
        ... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

        >>> quick = Butler(data)

        >>> quick.path_exists(['c','g',0,'k'])
        False
        >>> quick.path_exists(['c','g',0,'j'])
        True
        >>> Butler({'tricky': False}).path_exists(['tricky'])
        True
        """
        try:
            self[path]
            return True
        except KeyError:
            return False

    def key_list(self, sub_dict=None, output=None):
        """
        Flattens the sub_dict argument.
        Internal API used with find and findall functions.
        >>> data = {'a':10, 'b':[{'c':11, 'd': 13}, {'d':14, 'e':15}]}

        >>> quick = Butler(data)

        >>> quick.flatten(data)
        [('a', 10), ('b', [{'c': 11, 'd': 13}, {'e': 15, 'd': 14}]), (0, {'c': 11, 'd': 13}), ('c', 11), ('d', 13), (1, {'e': 15, 'd': 14}), ('e', 15), ('d', 14)]
        """
        if not sub_dict:
            sub_dict = self.data
        if not output:
            output = []
        for key in sub_dict:
            if isinstance(sub_dict[key], dict):
                self.flatten(sub_dict[key], output)
            if isinstance(sub_dict[key], list):
                for sub_dic in sub_dict[key]:
                    if isinstance(sub_dic, dict):
                        self.flatten(sub_dic, output)
            output.append(key)
        return output

    def flatten(self, sub_dict=None, output=None):
        """
        TODO: Make use of generators
        Flattens the sub_dict argument.
        Internal API used with find and findall functions.
        >>> data = {'a':10, 'b':[{'c':11, 'd': 13}, {'d':14, 'e':15}]}

        >>> quick = Butler(data)

        >>> quick.flatten(data)
        [('a', 10), ('b', [{'c': 11, 'd': 13}, {'e': 15, 'd': 14}]), (0, {'c': 11, 'd': 13}), ('c', 11), ('d', 13), (1, {'e': 15, 'd': 14}), ('e', 15), ('d', 14)]
        """
        if not sub_dict:
            sub_dict = self.data
        if not output:
            output = []
        if isinstance(sub_dict, dict):
            for key in sub_dict:
                output.append((key, sub_dict[key],))
                self.flatten(sub_dict[key], output)
        elif isinstance(sub_dict, list):
            for order, element in enumerate(sub_dict):
                output.append((order, element,))
                self.flatten(element, output)
        return output

    def findall(self, key, find=False):
        """
        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
        ... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

        >>> quick = Butler(data)

        >>> quick.findall('a')
        [1, 11]
        >>> new_list = [1, 2, 3, 4, [1,2,3,4], 5]

        >>> quick1 = Butler(new_list)

        >>> quick1.findall(4)
        [[1, 2, 3, 4]]

        >>> quick1.findall(5)
        [5]
        >>> Butler([{42: 'nope'}]).findall(42)
        ['nope']
        """
        return_list = []
        if isinstance(self.data, dict) or isinstance(self.data, list):
            flat_list = self.flatten(self.data)
            for item_key, data in flat_list:
                if item_key == key:
                    if find:  # API for find() to return the first result
                        return data
                    return_list.append(data)
        else:
            print("findall can be used only with dict or list objects")
        return return_list

    def find(self, key):
        """
        Works only with dict,
        Input
        key: The key to be searched for

        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
        ... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

        >>> quick = Butler(data)

        >>> quick.find('a')
        1
        >>> quick.find('e')
        5
        >>> quick.find('w')

        >>> new_list = [1, 2, 3, 4, 5]

        >>> quick1 = Butler(new_list)

        >>> quick1.find(2)
        3
        """
        data = self.findall(key, find=True)
        if data:
            return data
        return None

    def key_exists(self, key):
        """
        Uses find function to see if the requested key is in the dictionary
        Returns: True or False

        >>> data = {'a':1, 'b':2, 'c': {'d': 4, 'e': 5, 'f': [6, 7, 8], 'g':[{'h': 8, 'i': 9, 'j': 10}, {'a':11,
        ... 'b': 12, 'c': 13}]}, 'n': [14, 15, 16, 17, 18]}

        >>> quick = Butler(data)

        >>> quick.key_exists('a')
        True
        >>> quick.key_exists('w')
        False
        >>> Butler({'name': False}).key_exists('name')
        True
        """
        if key in self.key_list(self.data):
            return True
        else:
            return False

    def set(self, li, el):
        """
        Used to write to Butler objects. Makes it very easy to update and insert leaf nodes.
        ### Caution
        Returns True - Successful update or create
        Returns False - Failed due to non-existent path

        >>> a = {'b': {'c': {'d': 1, 's': 1001}}}
        >>> data = Butler(a)
        >>> data.set(['b', 'c', 'd'], 1001 )
        True
        >>> a
        {'b': {'c': {'s': 1001, 'd': 1001}}}
        >>> data.set(['b','c','s'], [10,100])
        True
        >>> a
        {'b': {'c': {'s': [10, 100], 'd': 1001}}}
        >>> data.data
        {'b': {'c': {'s': [10, 100], 'd': 1001}}}
        >>> data.set(['b','q','s'], [10,100])
        False
        >>> a
        {'b': {'c': {'s': [10, 100], 'd': 1001}}}
        >>> data.data
        {'b': {'c': {'s': [10, 100], 'd': 1001}}}
        >>> b = [[1, 2, 3], 4, 5]
        >>> data = Butler(b)
        >>> data.set([0], 1001)
        True
        >>> b
        [[1, 2, 3, 1001], 4, 5]
        >>> c = [[1, 2, 3], 4, 5]
        >>> data = Butler(c)
        >>> data.set([0,2], 1001)
        True
        >>> c
        [[1, 2, 1001], 4, 5]
        """
        try:
            self.__update__(self.data, li, el)
            return True
        except KeyError:
            return False

    def __update__(self, obj, li, el):
        """
        Recursive function used for updating the element or inserting the element if existing
        """
        if len(li) == 1:
            popped = li.pop()
            if type(obj[popped]) == list:
                obj[popped].append(el)
            else:
                obj[popped] = el
        else:
            x = li[0]
            return self.__update__(obj[x], li[1:], el)
        return True
