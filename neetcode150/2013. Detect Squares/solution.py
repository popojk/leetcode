"""
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
"""
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        # init a dict called points to store key: (x, y) value: count
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # add  1 to the dict in given X-Y axis
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        """
        Time: O(P), where P is the number of points
        Space: O(P), where P is the number of points
        """
        # init x1, y1 as xy value of point
        x1, y1 = point[0], point[1]
        # init res to store the result
        res = 0
        # iterate all point in points, if abs(x2 - x1) == abs(y2 - y1), it is a cross point
        for (x2, y2), n in self.points.items():
            x_dist = abs(x2-x1)
            y_dist = abs(y2-y1)
            # then we make corner point (x1, y2) and (x2, y1)
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                # if both corner points in points map, calculate possible squares by multiply amount of each 3 points
                if corner1 in self.points and corner2 in self.points:
                    res += n * self.points[corner1] * self.points[corner2]
        # return res
        return res

