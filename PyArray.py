class PyArray(list):
    def __init__(self, xs=None):
        if xs is not None:
            for item in xs:
                self.append(item)
        # set initial length of pyArray
        self.length = len(self)

    def push(self, item):
        self.append(item)
        self.length = len(self)
        return item

    def map(self, fn):
        return PyArray(map(fn, self))

    def filter(self, fn):
        return PyArray(filter(fn, self))

    def foreach(self, fn):
        for index, item in enumerate(self):
            fn(item, index)

    def reduce(self, fn):
        accum = None
        for index, item in enumerate(self):
            if index == 0:
                accum = item
            else:
                accum = fn(accum, item)
        return accum

    def includes(self, value):
        result = False
        for item in self:
            if item == value:
                result = True
        return result

    def every(self, fn):
        matches = []
        for item in self:
            if fn(item):
                matches.append(True)
            else:
                matches.append(False)
        return matches.count(True) == len(matches)

    def _find(self, fn):
        result = (None, None)
        for (index, item) in enumerate(self):
            if fn(item):
                result = (item, index)
                # item found, ignore all others
                break
        return result

    def find(self, fn):
        item, index = self._find(fn)
        return item

    def find_index(self, fn):
        item, index = self._find(fn)
        return index

    def join(self, separator=','):
        strings = [str(item) for item in self]
        return separator.join(strings)
