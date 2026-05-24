class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)  # use defaultdict always so that if a key doesnt exist and you access it -- it gets a default value of 0 and then you can just increment the count
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1  # count of given list point (list must be converted into a tuple to be a key of a map) increased by 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0  # initializing our result as 0
        px, py = point  # get x and y coordinate of a point
        for x, y in self.pts:  # iterate through all point in our map -- to go through all possible diagonal point
            if (abs(py - y) != abs(px - x)) or x == px or y == py:  # if their abs differences are different, meaning they CANNOT form a square! So we move on to the next iteration
                continue  # continue to next iteration. Must be diagonal inorder to form a square basically
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]  # both of these must exist in the map for it to be a square!

        return res