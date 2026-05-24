class TimeMap:

    def __init__(self):
        self.store = {}  # key = string, value = [list of lists is [value which is the string as key of hash, timestamps]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []  # if key is not already in the hashmap then we just add this key in our store first. We added key to our hashmap and added an empty list [] associated with that key.
        self.store[key].append([value, timestamp])  # now that we know self.store[key] exists, we can append the given values to it by dictonary[key].append()

    def get(self, key: str, timestamp: int) -> str:
        res = ""  # this is the empty string they want us to return in case the key doesnt exist in the hashmap.
        values = self.store.get(key, [])  # first get the values of the given key. In case that key is not there it will return default empty list []

        # Now we can perform the binary search
        l , r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2  # integer division ie // for whole number division / for decimal division.
            if values[m][1] <= timestamp:  # if the timestamp of values ie values[m][1] is less than the given timestamp then we:
                res = values[m][0]  # since it means its valid, we make res the values first item 0 as res
                l = m + 1  # we then move the left pointer to right as we wanna move to the right side of the array.
            else:  # if values timestamp is greater than the given time stamp:
                r = m - 1  # we move r to left by 1 as we wanna search in the left side now. Also this is an invalid case thats why res remains unchanged.
        
        return res
